from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver

from data.configuration import Configuration
from pageobjects.registration_page_actions import RegistrationPageActions


@pytest.fixture(scope="function")
def chrome_driver():
    def _chrome_driver(url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver
    yield _chrome_driver

@pytest.fixture(scope="function")
def fill_registration_details(chrome_driver):
    driver = chrome_driver(Configuration.web_url + Configuration.registration_endpoint)
    reg = RegistrationPageActions(driver)

    reg.fill_firstname(Configuration.firstname)
    reg.fill_lastname(Configuration.lastname)
    reg.select_date(Configuration.dob)
    reg.fill_street(Configuration.street)
    reg.fill_postal_code(Configuration.postal_code)
    reg.fill_city(Configuration.city)
    reg.fill_state(Configuration.state)
    reg.select_country(Configuration.country)
    reg.fill_phone(Configuration.phone)
    reg.fill_email(Configuration.email)
    reg.fill_password(Configuration.password)
    return driver


@pytest.fixture(scope="function")
def skip_registration_details(chrome_driver):
    driver = chrome_driver(Configuration.web_url + Configuration.registration_endpoint)
    reg = RegistrationPageActions(driver)

    reg.skip_firstname()
    reg.skip_lastname()
    reg.skip_email()
    reg.skip_password()

    reg.select_date(Configuration.dob)
    reg.fill_street(Configuration.street)
    reg.fill_postal_code(Configuration.postal_code)
    reg.fill_city(Configuration.city)
    reg.fill_state(Configuration.state)
    reg.select_country(Configuration.country)
    reg.fill_phone(Configuration.phone)

    return driver


@pytest.fixture(scope="function")
def check_for_invalid_email(chrome_driver):
    driver = chrome_driver(Configuration.web_url + Configuration.registration_endpoint)
    reg = RegistrationPageActions(driver)

    reg.fill_firstname(Configuration.firstname)
    reg.fill_lastname(Configuration.lastname)
    reg.select_date(Configuration.dob)
    reg.fill_street(Configuration.street)
    reg.fill_postal_code(Configuration.postal_code)
    reg.fill_city(Configuration.city)
    reg.fill_state(Configuration.state)
    reg.select_country(Configuration.country)
    reg.fill_phone(Configuration.phone)
    reg.fill_email(Configuration.invalid_email)
    reg.fill_password(Configuration.password)
    return driver


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    current_dir = Path(__file__).parent
    report_dir = current_dir / "reports" / today.strftime("%Y%m%d")

    # Ensure directory exists
    report_dir.mkdir(parents=True, exist_ok=True)

    # Define report path
    report_path = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"

    # Set pytest-html options
    config.option.htmlpath = str(report_path)
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "Tool Shop Registration Test Report"



