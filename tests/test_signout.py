import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SignInMain

class TestSignout:
    def test_signout(self, driver, wait):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*SignInMain.SUBMIT_BUTTON).click()
        driver.find_element(*SignInMain.NAME_INPUT).send_keys(*SignInMain.name_const)
        driver.find_element(*SignInMain.PASSWORD_INPUT).send_keys(*SignInMain.password_const)
        driver.find_element(*SignInMain.SUBMIT_BUTTON_SIGN_IN).click()
        driver.find_element(*SignInMain.SUBMIT_LK).click()

        logout_button = wait.until(EC.visibility_of_element_located(*SignInMain.SUBMIT_EXIT))
        driver.find_element(*SignInMain.SUBMIT_EXIT).click()

        login_button = wait.until(EC.presence_of_element_located(*SignInMain.SUBMIT_SIGNIN))

        after_logout_url = driver.current_url
        assert after_logout_url == 'https://stellarburgers.nomoreparties.site/login'
