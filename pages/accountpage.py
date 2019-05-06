from pages.custommethods import CustomMethods
from testdata.ExcelUtil import *


class AccountPage(CustomMethods):
    def __init__(self, driver):
        CustomMethods.__init__(self, driver)
        self.account_menu = "//span[text()='Accounts Menu']"
        self.new_account = "//span[text()='New Account']"
        record_type = read_test_data("Test_Data.xlsx", "Account_Data", "Record_Name")
        print(record_type)
        self.record_name = "(//span[text()=" + record_type + "])"
        self.account_name = "(//input[starts-with(@id,'input')])[3]"
        abn = read_test_data("Test_Data.xlsx", "Account_Data", "ABN")
        self.abn_exempt = "//option[@value=" + abn + "]"
        self.continue_button = "//button[text()='Continue']"
        self.parent_account = "//input[starts-with(@id,'209')]"
        self.phone_number = "//input[@type='tel']"
        self.revenue_select = "(//a[text()='--None--'])[1]"
        revenue = read_test_data("Test_Data.xlsx", "Account_Data", "Revenue_Area")
        self.revenue_group = "//a[@title=" + revenue + "]"
        wallet = read_test_data("Test_Data.xlsx", "Account_Data", "Wallet_Share")
        self.wallet_select = "//div[starts-with(@id, '1085')]"
        self.wallet_share = "//a[@title=" + wallet + "]"
        self.customer_segment = "//input[starts-with(@id,'2211')]"
        self.save_account = "//button[@title='Save']"
        global cm
        cm = CustomMethods(driver)

    def create_account(self):
        cm.short_wait()
        cm.perform_click('xpath', self.account_menu)
        cm.perform_click('xpath', self.new_account)
        cm.short_wait()
        cm.perform_scroll('xpath', self.record_name)
        cm.perform_click('xpath', self.record_name)
        account = read_test_data("Test_Data.xlsx", "Account_Data", "Account_Name")
        cm.enter('xpath', self.account_name, account)
        cm.click('xpath', self.abn_exempt)
        cm.click('xpath', self.continue_button)
        cm.short_wait()
        cm.click('xpath', self.parent_account)
        mobile = read_test_data("Test_Data.xlsx", "Account_Data", "Phone")
        cm.enter('xpath', self.phone_number, mobile)
        cm.click('xpath', self.revenue_select)
        cm.click('xpath', self.revenue_group)
        cm.click('xpath', self.wallet_select)
        cm.click('xpath', self.wallet_share)
        cus_segment = read_test_data("Test_Data.xlsx", "Account_Data", "Phone")
        cm.enter('xpath', self.customer_segment, cus_segment)
        cm.click('xpath', self.save_account)
