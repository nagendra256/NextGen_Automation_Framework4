from pages.custommethods import CustomMethods
from testdata.ExcelUtil import *


class SalesOrderPage(CustomMethods):
    def __init__(self, driver):
        CustomMethods.__init__(self, driver)
        self.driver = driver
        self.new_so = "//div[@title='New']"
        self.iframe = "//iframe[@title = 'accessibility title']"
        self.contact = "(//a[@class='select2-choice select2-default'])[1]"
        self.contact_name = "(//input[contains(@class,'select2-input')])[6]"
        self.line_item = "//span[text()='Line Items']"
        self.package = "//div[@title='Add Package']"
        package_name = read_test_data("Test_Data.xlsx", "SO_Data", "Package_Name")
        self.package_name = "(//a[contains(text()," + package_name + "])"
        product_name = read_test_data("Test_Data.xlsx", "SO_Data", "Product_Name")
        self.product = "//a[contains(text(), " + product_name + ")]"
        global cm
        cm = CustomMethods(driver)

    def xtend_package(self):
        cm.perform_click('xpath', self.new_so)
        cm.long_wait()
        cm.switch_to_frame('xpath', self.iframe)
        cm.click('xpath', self.contact)
        cm.click('xpath', self.contact_name)
        booking_contact = read_test_data("Test_Data.xlsx", "Contact_Data", "Contact")
        cm.enter('xpath', self.contact_name, booking_contact)
        cm.enter_key()
        cm.switch_to_default()
        cm.switch_to_frame('xpath', self.iframe)
        cm.click('xpath', self.line_item)
        cm.click()
        cm.switch_to_default()
        cm.switch_to_frame('xpath', self.iframe)
        cm.click('xpath', self.package)
        cm.long_wait()
        cm.switch_to_default()
        cm.switch_to_frame('xpath', self.iframe)
        cm.click('xpath', self.package_name)
        cm.action_click('xpath', self.product)
