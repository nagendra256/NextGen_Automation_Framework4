import pytest
import os
from testdata.ExcelUtil import *


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='test help')


@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver_path = os.getcwd().replace("\\", "/") + "/drivers/chromedriver.exe"
    browser = "chrome"
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=driver_path)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    data = read_test_data("Test_Data.xlsx", "Login_Data", "URL")
    print(data)
    driver.get(data)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    # driver.quit()
