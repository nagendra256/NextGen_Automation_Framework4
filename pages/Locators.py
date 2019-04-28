from selenium.webdriver.common.action_chains import ActionChains


class Locators:
    def __init__(self, driver):
        self.driver = driver

    def locator(self, locator_type, locator_value):
        try:

            if locator_type == "id":
                ele = self.driver.find_element_by_id(locator_value)
            elif locator_type == "name":
                ele = self.driver.find_element_by_name(locator_value)
            elif locator_type == "class":
                ele = self.driver.find_element_by_class_name(locator_value)
            elif locator_type == "xpath":
                ele = self.driver.find_element_by_xpath(locator_value)
            elif locator_type == "tag":
                ele = self.driver.find_element_by_tag_name(locator_value)
            return ele
        except:
            print("Locator not found")

    '''this method is to click on java script elements in salesforce CRM'''

    def perform_click(self, locator_type, locator_value):
        e = self.locator(locator_type, locator_value)
        op = self.driver.execute_script('arguments[0].click()', e)

    '''this method is to scroll into the particular element'''

    def perform_scroll(self, locator_type, locator_value):
        e = self.locator(locator_type, locator_value)
        op = self.driver.execute_script("arguments[0].scrollIntoView();", e)

    '''this action chain method is to perform mouse hover and click on web element'''

    def action_click(self, locator_type, locator_value):
        e = self.locator(locator_type, locator_value)
        action = ActionChains(self.driver)
        ac = action.move_to_element(e).click()
        ac.click()
