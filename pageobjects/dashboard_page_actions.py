import time

from utilities.wait_utils import WaitUtils
from pageobjects.base_page import BasePage
from locators.dashboard_page import DashboardPage

class DashboardPageActions(BasePage):

    def search_prod(self, prod_name):
        element = WaitUtils.wait_for_element(self.driver, DashboardPage.search_field_xpath)
        element.send_keys(prod_name)