import logging
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.base_page import BasePage
from locators.registration_page import RegistrationPage
from utilities.wait_utils import WaitUtils

log = logging.getLogger(__name__)


def log_fixture():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("report.html", mode="w")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

class RegistrationPageActions(BasePage):
    def fill_firstname(self, firstname):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.first_name_locator)
        element.clear()
        element.send_keys(firstname)

    def skip_firstname(self):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.first_name_locator)
        element.clear()

    def fill_lastname(self, lastname):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.last_name_locator)
        element.clear()
        element.send_keys(lastname)

    def skip_lastname(self):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.last_name_locator)
        element.clear()


    def select_date(self, date):
        element = WaitUtils.wait_for_clickable(self.driver, RegistrationPage.dob_locator)
        element.clear()
        element.send_keys(date)

    def fill_street(self, street):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.street_locator)
        element.clear()
        element.send_keys(street)

    def fill_postal_code(self, postalcode):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.postal_code_locator)
        element.clear()
        element.send_keys(postalcode)

    def fill_city(self, city):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.city_locator)
        element.clear()
        element.send_keys(city)

    def fill_state(self, state):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.state_locator)
        element.clear()
        element.send_keys(state)

    def select_country(self, country):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.country_locator)
        country_dropdown = Select(element)
        country_dropdown.select_by_visible_text(country)

    def fill_phone(self, phone):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.phone_locator)
        element.clear()
        element.send_keys(phone)

    def fill_email(self, email):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.email_locator)
        element.clear()
        element.send_keys(email)

    def skip_email(self):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.email_locator)
        element.clear()

    def fill_wrong_email_format(self, wrong_email):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.email_locator)
        element.clear()
        element.send_keys(wrong_email)

    def fill_password(self, password):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.password_locator)
        element.clear()
        element.send_keys(password)

    def skip_password(self):
        element = WaitUtils.wait_for_element(self.driver, RegistrationPage.password_locator)
        element.clear()

    def regd(self):
        element = WaitUtils.wait_for_clickable(self.driver, RegistrationPage.register_button_locator)
        element.click()

    def check_registration_errors(self):
        try:
            error_block = WaitUtils.wait_for_element(self.driver, RegistrationPage.registration_error_locator,timeout=5)
            if error_block:
                error_message = error_block.text
                log.error(f"Registration Error: {error_message}")
                print(f"Registration Error: {error_message}")
                return True, error_message
            else:
                return False, None
        except Exception as e:
            log.warning(f"No registration errors found or element not located: {e}")
            return False, None

    def detect_weak_password(self):
        password_detection_element = WaitUtils.wait_for_element(self.driver, RegistrationPage.password_detection_locator)

        if password_detection_element:
            return True
        else:
            return False


    def detection_skip_fields(self):
        firstname_element = WaitUtils.wait_for_element(self.driver, RegistrationPage.firstname_blank_locator)
        lastname_element = WaitUtils.wait_for_element(self.driver, RegistrationPage.lastname_blank_locator)
        email_element = WaitUtils.wait_for_element(self.driver, RegistrationPage.email_blank_locator)
        password_element = WaitUtils.wait_for_element(self.driver, RegistrationPage.password_blank_locator)

        if all([firstname_element, lastname_element, email_element, password_element]):
            return True
        else:
            return False

    def check_email_validity(self, email):
        try:
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            # email_element = WaitUtils.wait_for_element(self.driver, RegistrationPage.email_blank_locator)

            if re.fullmatch(email_regex, email):
                return True
            else:
                return False
        except Exception as e:
            return False

