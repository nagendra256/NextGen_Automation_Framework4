from pages.custommethods import CustomMethods
from testdata.ExcelUtil import *


class LoginPage(CustomMethods):
    def __init__(self, driver):
        CustomMethods.__init__(self, driver)
        self.user_name = "username"
        self.password = "password"
        self.login_button = "Login"
        global cm
        cm = CustomMethods(driver)

    def login_salesforce(self):
        un = read_test_data("Test_Data.xlsx", "Login_Data", "User_Name")
        cm.enter('id', self.user_name, un)
        pwd = read_test_data("Test_Data.xlsx", "Login_Data", "Password")
        cm.enter('id', self.password, pwd)
        cm.click('id', self.login_button)
