from pages.loginpage import LoginPage
from pages.accountpage import AccountPage
import pytest
import time

@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_login(self):
        driver = self.driver
        lp = LoginPage(driver)
        lp.login_salesforce()

    def test_account(self):
        driver = self.driver
        hp = AccountPage(driver)
        hp.create_account()