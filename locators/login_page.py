from selenium.webdriver.common.by import By


class LoginPage:
    email_locator = (By.XPATH, "//input[@id='email']")
    password_locator = (By.XPATH, "//input[@id='password']")
    eye_button_locator = (By.XPATH, "//button[@class='btn btn-outline-secondary']")
    login_button_locator = (By.XPATH, "//input[@data-test='login-submit']")
    registration_page_locator = (By.XPATH, "//a[contains(text(), 'Register your account')]")
    forget_password_page_locator = (By.XPATH, "//a[contains(text(), 'Forgot your Password?')]")
    login_error_locator = (By.XPATH, "//div[@class='help-block']")
    email_blank_locator = (By.XPATH, "//div[@data-test='email-error']")
    password_blank_locator = (By.XPATH, "//div[@data-test='password-error']")
