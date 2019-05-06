from pages.Locators import Locators
import time
from testdata.ExcelUtil import *
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class CustomMethods(Locators):
    def __init__(self, driver):
        self.driver = driver
        Locators.__init__(self, driver)
        global loc
        loc = Locators(driver)

    def enter(self, locator_type, locator_value, input_data):
        e = self.locator(locator_type, locator_value)
        e.send_keys(input_data)

    def click(self, locator_type, locator_value):
        e = self.locator(locator_type, locator_value)
        e.click()

    def extract_data(self, locator_type, locator_value):
        e = self.locator(locator_type, locator_value)
        e.get_attribute("value")

    def short_wait(self):
        time.sleep(15)

    def long_wait(self):
        time.sleep(45)

    def enter_key(self, locator_type, locator_value):
        e = self.locator(locator_type, locator_value)
        e.send_keys(Keys.ENTER)
