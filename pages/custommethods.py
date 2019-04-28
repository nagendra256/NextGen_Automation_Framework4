from pages.Locators import Locators
import time
import allure


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

    def custom_wait(self):
        time.sleep(15)
