from datetime import datetime
import logging
import os
from pprint import pprint
import random
import requests
import time

from mintamazontagger.currency import micro_usd_to_float_usd
from mintamazontagger.webdriver import (
    get_element_by_id, get_element_by_xpath,
    get_element_by_link_text, get_elements_by_class_name,
    is_visible)

from selenium.common.exceptions import (
    ElementNotInteractableException, StaleElementReferenceException,
    TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)

MINT_API_VERSION = 'pfm/v1'

MINT_HOME = 'https://mint.intuit.com'
MINT_OVERVIEW = f'{MINT_HOME}/overview'
MINT_TRANSACTIONS = f'{MINT_HOME}/{MINT_API_VERSION}/transactions'
MINT_CATEGORIES = f'{MINT_HOME}/{MINT_API_VERSION}/categories'


class MintClient():
    args = None
    webdriver_factory = None
    mfa_input_callback = None
    request_id = 0
    webdriver = None
    logged_in = False

    def __init__(self, args, webdriver_factory, mfa_input_callback=None):
        self.args = args
        self.webdriver_factory = webdriver_factory
        self.mfa_input_callback = mfa_input_callback

    def hasValidCredentialsForLogin(self):
        if self.args.mint_user_will_login:
            return True
        return self.args.mint_email and self.args.mint_password

    def get_api_header(self):
        return _get_api_header(self.webdriver)

    def login(self):
        if self.logged_in:
            return True
        if not self.hasValidCredentialsForLogin():
            logger.error('Missing Mint email or password.')
            return False

        logger.info('You may be asked for an auth code at the command line! '
                    'Be sure to press ENTER after typing the 6 digit code.')

        self.webdriver = self.webdriver_factory()
        self.logged_in = _nav_to_mint_and_login(
            self.webdriver, self.args, self.mfa_input_callback)
        _wait_for_overview_loaded(self.webdriver, self.args.mint_wait_for_sync)
        return self.logged_in

    def get_transactions(self, from_date=None, to_date=None):
        if not self.login():
            logger.error('Cannot login')
            return []
        logger.info(
            f'Getting all Mint transactions since {from_date} to {to_date}.')
        params = {
            'limit': '100000',
            'fromDate': from_date,
            'toDate': to_date,
        }

        response = self.webdriver.request(
            'GET', MINT_TRANSACTIONS, headers=self.get_api_header(),
            params=params)
        if not _is_json_response_success('transactions', response):
            return []
        response_json = response.json()
        if not response_json['metaData']['totalSize']:
            logger.warning('No transactions found')
            return []
        if (response_json['metaData']['totalSize']
                > response_json['metaData']['pageSize']):
            # TODO(jprouty): Add pagination support.
            # Look at: response_json['metaData']['link'][1]['href']
            logger.error('More transactions are available than max page size '
                         '- try reducing the date range.')
        if self.args.mint_save_json:
            json_path = os.path.join(
                self.args.mint_json_location,
                f'Mint {int(time.time())} Transactions.json')
            logger.info(f'Saving Mint Transactions to json file: {json_path}')
            with open(json_path, "w") as json_out:
                pprint(response_json, json_out)
        # Remove all transactions that do not have a fiData message. These are
        # user entered expesnes and do not have a fiData entry.
        result = [trans for trans in response_json['Transaction']
                  if 'fiData' in trans]
        return result

    def get_categories(self):
        if not self.login():
            logger.error('Cannot login')
            return []
        logger.info('Getting Mint categories.')

        response = self.webdriver.request(
            'GET', MINT_CATEGORIES, headers=self.get_api_header())
        if not _is_json_response_success('categories', response):
            return []
        response_json = response.json()
        if not response_json['metaData']['totalSize']:
            logger.error('No categories found')
            return []
        if self.args.mint_save_json:
            json_path = os.path.join(
                self.args.mint_json_location,
                f'Mint {int(time.time())} Categories.json')
            logger.info(f'Saving Mint Categories to json file: {json_path}')
            with open(json_path, "w") as json_out:
                pprint(response_json, json_out)
        result = {}
        for cat in response_json['Category']:
            result[cat['name']] = cat
        return result

    def send_updates(self, updates, progress, ignore_category=False):
        if not self.login():
            logger.error('Cannot login')
            return 0
        num_requests = 0
        for (orig_trans, new_trans) in updates:
            if len(new_trans) == 1:
                # Update the existing transaction.
                trans = new_trans[0]
                modify_trans = {
                    'type': trans.type,
                    'description': trans.description,
                    'notes': trans.notes,
                }
                if not ignore_category:
                    modify_trans = {
                        **modify_trans,
                        'category': {'id': trans.category.id},
                    }

                logger.debug(
                    f'Sending a "modify" transaction request: {modify_trans}')
                response = self.webdriver.request(
                    'PUT',
                    f'{MINT_TRANSACTIONS}/{trans.id}',
                    json=modify_trans,
                    headers=self.get_api_header())
                logger.debug(f'Received response: {response.__dict__}')
                progress.next()
                num_requests += 1
            else:
                # Split the existing transaction into many.
                split_children = []
                for trans in new_trans:
                    category = (orig_trans.category if ignore_category
                                else trans.category)
                    itemized_split = {
                        'amount': f'{micro_usd_to_float_usd(trans.amount)}',
                        'description': trans.description,
                        'category': {'id': category.id, 'name': category.name},
                        'notes': trans.notes,
                    }
                    split_children.append(itemized_split)

                split_edit = {
                    'type': orig_trans.type,
                    'amount': micro_usd_to_float_usd(orig_trans.amount),
                    'splitData': {'children': split_children},
                }
                logger.debug(
                    f'Sending a "split" transaction request: {split_edit}')
                response = self.webdriver.request(
                    'PUT',
                    f'{MINT_TRANSACTIONS}/{trans.id}',
                    json=split_edit,
                    headers=self.get_api_header())
                logger.debug(f'Received response: {response.__dict__}')
                progress.next()
                num_requests += 1

        progress.finish()
        return num_requests


def _is_json_response_success(request_string, response):
    if response.status_code != requests.codes.ok:
        logger.error(
            f'Error getting {request_string}. '
            f'status_code = {response.status_code}')
        return False
    content_type = response.headers.get('content-type', '')
    if not content_type.startswith('application/json'):
        logger.error(
            f'Error getting {request_string}. content_type = {content_type}')
        return False
    return True


# Never attempt to enter the password more than 2 times to prevent locking an
# account out due to too many fail attempts. A valid MFA can require reentry
# of the password.
_MAX_PASSWORD_ATTEMPTS = 2


def _nav_to_mint_and_login(webdriver, args, mfa_input_callback=None):
    logger.info('Mint Login Flow: Navigating to Mint homepage.')
    webdriver.get(MINT_HOME)
    webdriver.implicitly_wait(0)

    sign_in_button = get_element_by_link_text(webdriver, 'Sign in')
    if not sign_in_button:
        logger.error('Mint Login Flow: Cannot find "Sign in" button.')
        return False
    logger.info('Mint Login Flow: Clicking "Sign in" button.')
    sign_in_button.click()

    # Logging in to mint.com is a bit messy. Work through the flow,
    # allowing for any order of interstitials. Exit only when reaching the
    # overview page (indicating the user is logged in) or if the Logging in to
    # mint.com timeout has been exceeded.
    #
    # For each attempt section, note that the element must both be present AND
    # visible. Mint renders but hides the complete "Logging in to mint.com"
    # flow meaning that all elements are always present (but only a subset are
    # visible at any moment).
    login_start_time = datetime.now()
    num_password_attempts = 0
    while not webdriver.current_url.startswith(MINT_OVERVIEW):
        since_start = datetime.now() - login_start_time
        if (args.mint_login_timeout
                and since_start.total_seconds() > args.mint_login_timeout):
            logger.error('Mint Login Flow: Exceeded login timeout')
            return False

        if args.mint_user_will_login:
            logger.info('Mint Login Flow: login to be performed by user')
            _login_flow_advance(webdriver)
            continue

        try:
            userid_input = get_element_by_id(webdriver, 'ius-userid')
            identifier_input = get_element_by_id(webdriver, 'ius-identifier')
            identifier_first_input = get_element_by_id(
                webdriver, 'iux-identifier-first-unknown-identifier')
            ius_text_input = get_element_by_id(webdriver, 'ius-text-input')
            password_input = get_element_by_id(webdriver, 'ius-password')
            submit_button = get_element_by_id(
                webdriver, 'ius-sign-in-submit-btn')
            first_submit_button = get_element_by_id(
                webdriver, 'ius-identifier-first-submit-btn')
            # Password might be asked later in the MFA flow.
            mfa_password_input = get_element_by_id(
                webdriver,
                'ius-sign-in-mfa-password-collection-current-password')
            mfa_submit_button = get_element_by_id(
                webdriver, 'ius-sign-in-mfa-password-collection-continue-btn')
            # New MFA flow for password - uses mfa_continue_button to continue.
            password_verification_input = get_element_by_id(
                webdriver, 'iux-password-verification-password')
            mfa_continue_button = get_element_by_xpath(
                webdriver, '//button/span[text()="Continue"]')
            sign_in_button = get_element_by_xpath(
                webdriver, '//button/span[text()="Sign In"]')
            # New flow for password as if 9/29/2022 - uses mfa_continue_button
            # to continue.
            confirmation_password_input = get_element_by_id(
                webdriver, 'iux-password-confirmation-password')

            # Attempt to enter an email and/or password if the fields are
            # present.
            do_submit = False
            if is_visible(userid_input):
                userid_input.clear()
                userid_input.send_keys(args.mint_email)
                logger.info(
                    'Mint Login Flow: Entering email into "userid" field')
                do_submit = True
            if is_visible(identifier_input):
                identifier_input.clear()
                identifier_input.send_keys(args.mint_email)
                logger.info('Mint Login Flow: Entering email into "id" field')
                do_submit = True
            if is_visible(identifier_first_input):
                identifier_first_input.clear()
                identifier_first_input.send_keys(args.mint_email)
                logger.info(
                    'Mint Login Flow: Entering email into first "id" field')
                do_submit = True
            if is_visible(ius_text_input):
                ius_text_input.clear()
                ius_text_input.send_keys(args.mint_email)
                logger.info(
                    'Mint Login Flow: Entering email into "text" field')
                do_submit = True
            if is_visible(password_input):
                num_password_attempts += 1
                password_input.clear()
                password_input.send_keys(args.mint_password)
                logger.info('Mint Login Flow: Entering password')
                do_submit = True
            if is_visible(password_verification_input):
                num_password_attempts += 1
                password_verification_input.clear()
                password_verification_input.send_keys(args.mint_password)
                logger.info(
                    'Mint Login Flow: Entering password in verification')
                do_submit = True
            if is_visible(mfa_password_input):
                num_password_attempts += 1
                mfa_password_input.clear()
                mfa_password_input.send_keys(args.mint_password)
                logger.info('Mint Login Flow: Entering password in MFA input')
                do_submit = True
            if is_visible(confirmation_password_input):
                num_password_attempts += 1
                confirmation_password_input.clear()
                confirmation_password_input.send_keys(args.mint_password)
                logger.info('Mint Login Flow: Entering password in '
                            'confirmation password input')
                do_submit = True
            if num_password_attempts > _MAX_PASSWORD_ATTEMPTS:
                logger.error(
                    'Mint Login Flow: Too many password attempts; aborting.')
                return False
            if do_submit:
                if is_visible(submit_button):
                    logger.info(
                        'Mint Login Flow: Submitting login credentials')
                    submit_button.submit()
                elif is_visible(mfa_submit_button):
                    logger.info(
                        'Mint Login Flow: Submitting credentials for MFA')
                    mfa_submit_button.submit()
                elif is_visible(first_submit_button):
                    logger.info(
                        'Mint Login Flow: Submitting credentials for MFA')
                    first_submit_button.click()
                elif is_visible(mfa_continue_button):
                    logger.info(
                        'Mint Login Flow: Submitting credentials for password '
                        'verification')
                    mfa_continue_button.click()
                elif is_visible(sign_in_button):
                    logger.info(
                        'Mint Login Flow: Submitting via "Sign in"')
                    sign_in_button.click()
                else:
                    logger.error('Mint Login Flow: Cannot find submit button!')

                _login_flow_advance(webdriver)
                continue

            # Attempt to find the email on the account list page. This is often
            # the case when reusing a webdriver that has session state from a
            # previous run of the tool.
            known_accounts_selector = get_element_by_id(
                webdriver, 'ius-known-accounts-container')
            if is_visible(known_accounts_selector):
                usernames = get_elements_by_class_name(
                    webdriver, 'ius-option-username')
                found_username = False
                for username in usernames:
                    if username.text == args.mint_email:
                        found_username = True
                        logger.info(
                            'Mint Login Flow: Selecting username from '
                            'multi-account selector.')
                        username.click()
                        break
                if found_username:
                    _login_flow_advance(webdriver)
                    continue

                # The provided email is not in the known accounts list. Go
                # through the 'Use a different user ID' flow:
                use_different_account_button = get_element_by_id(
                    webdriver, 'ius-known-device-use-a-different-id')
                if not is_visible(use_different_account_button):
                    logger.error(
                        'Mint Login Flow: Cannot locate add account button.')
                    return False
                logger.info(
                    'Mint Login Flow: Selecting "Different user" from '
                    'multi-account selector.')
                use_different_account_button.click()
                _login_flow_advance(webdriver)
                continue

            # If shown, bypass the "Let's add your current mobile number"
            # modal.
            skip_phone_update_button = get_element_by_id(
                webdriver, 'ius-verified-user-update-btn-skip')
            if is_visible(skip_phone_update_button):
                logger.info(
                    'Mint Login Flow: '
                    'Skipping update user phone number modal.')
                skip_phone_update_button.click()
                _login_flow_advance(webdriver)
                continue

            # MFA method selector:
            mfa_options_form = get_element_by_id(
                webdriver, 'ius-mfa-options-form')
            if is_visible(mfa_options_form):
                # Attempt to use the user preferred method, falling back to the
                # first method.
                mfa_method_option = get_element_by_id(
                    webdriver,
                    f'ius-mfa-option-{args.mint_mfa_preferred_method}')
                if is_visible(mfa_method_option):
                    mfa_method_option.click()
                    logger.info(
                        'Mint Login Flow: '
                        f'Selecting {args.mint_mfa_preferred_method} '
                        'MFA method')
                else:
                    mfa_method_cards = get_elements_by_class_name(
                        webdriver, 'ius-mfa-card-challenge')
                    if mfa_method_cards and len(mfa_method_cards) > 0:
                        mfa_method_cards[0].click()
                mfa_method_submit = get_element_by_id(
                    webdriver, 'ius-mfa-options-submit-btn')
                if is_visible(mfa_method_submit):
                    logger.info('Mint Login Flow: Submitting MFA method')
                    mfa_method_submit.click()
                    _login_flow_advance(webdriver)
                    continue

            # MFA OTP Code - uses mfa_continue_button to continue.
            mfa_code_input = get_element_by_id(
                webdriver, 'ius-mfa-confirm-code')
            if is_visible(mfa_code_input) and is_visible(mfa_continue_button):
                mfa_code = (mfa_input_callback or input)(
                    'Please enter your 6-digit MFA code: ')
                logger.info('Mint Login Flow: Entering MFA OTP code')
                mfa_code_input.send_keys(mfa_code)
                logger.info('Mint Login Flow: Submitting MFA OTP')
                mfa_continue_button.click()
                _login_flow_advance(webdriver)
                continue

            # MFA soft token:
            mfa_token_input = get_element_by_id(
                webdriver, 'ius-mfa-soft-token')
            mfa_token_submit_button = get_element_by_id(
                webdriver, 'ius-mfa-soft-token-submit-btn')
            if is_visible(mfa_token_input) and is_visible(
                    mfa_token_submit_button):
                import oathtool
                logger.info('Mint Login Flow: Generating soft token')
                mfa_code = oathtool.generate_otp(args.mfa_soft_token)
                logger.info(
                    'Mint Login Flow: Entering soft token into MFA input')
                mfa_token_input.send_keys(mfa_code)
                logger.info('Mint Login Flow: Submitting soft token MFA')
                mfa_token_submit_button.submit()
                _login_flow_advance(webdriver)
                continue

            # MFA account selector:
            mfa_select_account = get_element_by_id(
                webdriver, 'ius-mfa-select-account-section')
            continue_button = get_element_by_xpath(
                webdriver, '//button[text()=\'Continue\']')
            if is_visible(mfa_select_account):
                account = args.mint_intuit_account or args.mint_email
                logger.info('Mint Login Flow: MFA select intuit account')

                account_input = get_element_by_xpath(
                    webdriver,
                    f'//label/span/div/span[text()=\'{account}\']')
                if (is_visible(account_input)
                        and is_visible(mfa_token_submit_button)):
                    logger.info('Mint Login Flow: MFA account selection')
                    account_input.click()
                    continue_button.click()
                    _login_flow_advance(webdriver)
                    continue
                else:
                    logger.error(
                        'Mint Login Flow: '
                        'Cannot find matching mint intuit account.')

            # Multiple intuit accounts for email address.
            select_account = get_element_by_id(
                webdriver, 'ius-select-account-radio-option-0-input')
            # select_account_submit_button = get_element_by_xpath(
            #     webdriver, '//button[text()=\'Continue\']')
            if is_visible(select_account):
                account = args.mint_intuit_account or args.mint_email
                logger.info(
                    'Mint Login Flow: '
                    'Select Intuit account from email (multiple present)')

                account_input = get_element_by_xpath(
                    webdriver,
                    f'//label/span/div/span[text()=\'{account}\']')
                if is_visible(account_input) and is_visible(continue_button):
                    logger.info('Mint Login Flow: Found matching account')
                    account_input.click()
                    continue_button.click()
                    _login_flow_advance(webdriver)
                    continue
                else:
                    logger.error(
                        'Mint Login Flow: '
                        'Cannot find matching mint intuit account.')

            # Skip modal asking for passwordless login.
            skip_web_authn_reg_button = get_element_by_id(
                webdriver, 'skipWebauthnRegistration')
            if is_visible(skip_web_authn_reg_button):
                logger.info(
                    'Mint Login Flow: Skipping Passwordless Registration.')
                skip_web_authn_reg_button.click()
                continue

        except StaleElementReferenceException:
            logger.warning(
                'Mint Login Flow: Page contents changed - trying again.')
        except ElementNotInteractableException:
            logger.warning(
                'Mint Login Flow: '
                'Page contents not interactable - trying again.')

    logger.info('Mint Login Flow: login successful.')
    # If you made it here, you must be good to go!
    return True


def _login_flow_advance(webdriver):
    time.sleep(random.randint(500, 1500) / 1000)


def _wait_for_overview_loaded(
        webdriver, wait_for_sync=False, wait_for_sync_timeout=5 * 60):
    logger.info('Waiting for Mint Overview')
    try:
        # Wait for the accounts list to present before continuing.
        WebDriverWait(webdriver, 30).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, '//span[text()="Accounts"]')))
        logger.info('Mint overview loaded')
        if (wait_for_sync):
            logger.info('Waiting for Mint to sync accounts')
            WebDriverWait(webdriver, wait_for_sync_timeout).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH,
                     '//strong[text()="Account refresh complete."]')))
            logger.info('Mint account sync complete')
    except (TimeoutException, StaleElementReferenceException):
        logger.warning("Mint sync apparently incomplete after timeout. "
                       "Data retrieved may not be current.")


def _get_api_header(webdriver):
    api_key = webdriver.execute_script(
        "return window.__shellInternal.appExperience.appApiKey")
    auth = f'Intuit_APIKey intuit_apikey={api_key}, intuit_apikey_version=1.0'
    return {
        'authorization': auth,
        'accept': 'application/json',
    }
