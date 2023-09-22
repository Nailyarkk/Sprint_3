import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from locators import SignInMain
import pytest
from constants import *
class TestSignin:

    def wait(self, driver):
        return WebDriverWait(driver, 10)

    def checkauth(self, driver):
        driver.find_element(*SignInMain.SUBMIT_LK).click()
        name = driver.find_element(*SignInMain.CURR_NAME)
        value_attribute = name.get_attribute('value')
        assert value_attribute == name_const

    @pytest.mark.parametrize("url, submit_selector", [
        ("https://stellarburgers.nomoreparties.site/", SignInMain.SUBMIT_BUTTON),
        ("https://stellarburgers.nomoreparties.site/", SignInMain.SUBMIT_TEXT_LK),
        ("https://stellarburgers.nomoreparties.site/register", SignInMain.SUBMIT_LOGIN),
        ("https://stellarburgers.nomoreparties.site/forgot-password", SignInMain.SUBMIT_LOGIN)
    ])
    def test_checkauth(self, driver, auth,url, submit_selector):
        auth(url, submit_selector)
        self.checkauth(driver)
