from selenium.webdriver.common.by import By


class RegistrationPage:
    first_name_locator = (By.ID, 'first_name')
    last_name_locator = (By.ID, 'last_name')
    dob_locator = (By.ID, 'dob')
    street_locator = (By.ID, 'street')
    postal_code_locator = (By.ID, 'postal_code')
    city_locator = (By.ID, 'city')
    state_locator = (By.ID, 'state')
    phone_locator = (By.ID, 'phone')
    email_locator = (By.ID, 'email')
    password_locator = (By.ID, 'password')
    register_button_locator = (By.XPATH, "//button[@data-test='register-submit']")
    country_locator = (By.XPATH, "//select[@id='country']")
    registration_error_locator = (By.XPATH, "//div[@class='help-block']")
    # save_address_locator = (By.XPATH, "//div[contains(text(), 'Save address?')]")
    # no_thanks_button = (By.XPATH, ".//button[contains(text(), 'No thanks')]")'
    password_detection_locator = (By.XPATH, "//div[@class='fill weak']")
    firstname_blank_locator = (By.XPATH, "//div[@data-test='first-name-error']")
    lastname_blank_locator = (By.XPATH, "//div[@data-test='last-name-error']")
    email_blank_locator = (By.XPATH, "//div[@data-test='email-error']")
    password_blank_locator = (By.XPATH, "//div[@data-test='password-error']")