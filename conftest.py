import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SignInMain
import time
from constants import *
@pytest.fixture(scope="function")
def driver():
    chrome_service = Service('chromedriver/chromedriver')
    driver = WebDriver(service=chrome_service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def auth( driver):
    def _auth(url, loc):
        driver.get(url)
        driver.find_element(*loc).click()
        driver.find_element(*SignInMain.NAME_INPUT).send_keys(name_const)
        driver.find_element(*SignInMain.PASSWORD_INPUT).send_keys(password_const)
        driver.find_element(*SignInMain.SUBMIT_BUTTON_SIGN_IN).click()

    return _auth

