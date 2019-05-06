from pages.loginpage import LoginPage
from pages.accountpage import AccountPage
from pages.contactpage import ContactPage
from pages.opportunitypage import OpportunityPage
from pages.salesorderpage import SalesOrderPage
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

    def test_contact(self):
        driver = self.driver
        cp = ContactPage(driver)
        cp.create_contact()

    def test_opportunity(self):
        driver = self.driver
        op = OpportunityPage(driver)
        op.create_opportunity()

    def test_create_order(self):
        driver = self.driver
        sp = SalesOrderPage(driver)
        sp.xtend_package()
