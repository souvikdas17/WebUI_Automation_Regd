import pytest
import logging

from data.configuration import Configuration
from pageobjects.registration_page_actions import RegistrationPageActions

log = logging.getLogger(__name__)


class TestRegistration:

    @pytest.mark.registration
    def test_01_successful_registration(self, fill_registration_details):
        try:
            self.driver = fill_registration_details
            reg = RegistrationPageActions(driver=self.driver)

            log.info("Registration page opens")
            reg.regd()
            log.info("Registration Successful")
            print("Registration Successful")
        except Exception as e:
            raise AssertionError(f"Error occurred: {e}")
        finally:
            self.driver.quit()

    @pytest.mark.registration
    def test_02_register_using_existing_email(self, fill_registration_details):
        try:
            self.driver = fill_registration_details
            reg = RegistrationPageActions(self.driver)

            reg.fill_email(Configuration.email)
            reg.regd()
            print("Email already exists")
            log.info("Email already exists")
        except Exception as err:
            raise AssertionError(f"Error occurred: {err}")
        finally:
            self.driver.quit()

    @pytest.mark.registration
    def test_03_weak_password_detection(self, fill_registration_details):
        try:
            self.driver = fill_registration_details
            reg = RegistrationPageActions(self.driver)

            reg.fill_password(Configuration.weak_password)
            reg.regd()

            has_weak_password = reg.detect_weak_password()

            if has_weak_password:
                log.error("Password must contain at least 6 characters, including letters and numbers.")
                print("Password must contain at least 6 characters, including letters and numbers.")
            else:
                print("Please provide a weak password to run testcase :- Detect Weak Password")

        except Exception as err:
            raise AssertionError(f"Error occurred: {err}")
        finally:
            self.driver.quit()

    @pytest.mark.registration
    def test_04_missing_required_fields(self, skip_registration_details):
        try:
            self.driver = skip_registration_details
            reg = RegistrationPageActions(self.driver)

            reg.regd()

            has_blank_fields = reg.detection_skip_fields()

            if has_blank_fields:
                log.error("Firstname, Lastname, Email-id, Password all of this fields are required")
                print("Firstname, Lastname, Email-id, Password all of this fields are required")
            else:
                print("Please skip username, email and password to run testcase :- Detect Required Fields")
        except Exception as err:
            raise AssertionError(f"Error occurred: {err}")
        finally:
            self.driver.quit()

    @pytest.mark.registration
    def test_05_invalid_imail_format(self, check_for_invalid_email ):
        try:
            self.driver = check_for_invalid_email
            reg = RegistrationPageActions(self.driver)

            reg.regd()

            has_invalid_email = reg.check_email_validity(Configuration.invalid_email)

            if not has_invalid_email:
                log.error("Please enter a valid email address.")
                print("Please enter a valid email address.")
            else:
                print("Please enter a invalid email to run testcase :- Invalid Email Format")

        except Exception as err:
            raise AssertionError(f"Error occurred: {err}")
        finally:
            self.driver.quit()

