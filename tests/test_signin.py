import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from locators import SignInMain

class TestSignin:

    @pytest.mark.usefixtures("driver", "wait")
    def test_signin_main(self,driver, wait):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*SignInMain.SUBMIT_BUTTON).click()
        driver.find_element(*SignInMain.NAME_INPUT).send_keys(*SignInMain.name_const)
        driver.find_element(*SignInMain.PASSWORD_INPUT).send_keys(*SignInMain.password_const)
        driver.find_element(*SignInMain.SUBMIT_BUTTON_SIGN_IN).click()
        driver.find_element(*SignInMain.SUBMIT_LK).click()

        element = wait.until(EC.presence_of_element_located(*SignInMain.element_value))
        name = driver.find_element(*SignInMain.CURR_NAME)
        value_attribute = name.get_attribute('value')
        assert value_attribute == 'nailyarkk@ya.ru'



    @pytest.mark.usefixtures("driver", "wait")
    def test_signin_button_LK(self, driver, wait):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*SignInMain.SUBMIT_TEXT_LK).click()
        driver.find_element(*SignInMain.NAME_INPUT).send_keys(*SignInMain.name_const)
        driver.find_element(*SignInMain.PASSWORD_INPUT).send_keys(*SignInMain.password_const)
        driver.find_element(*SignInMain.SUBMIT_BUTTON_SIGN_IN).click()
        driver.find_element(*SignInMain.SUBMIT_LK).click()
        element = wait.until(EC.presence_of_element_located(*SignInMain.element_value))

        name = driver.find_element(*SignInMain.CURR_NAME)
        value_attribute = name.get_attribute('value')

        assert value_attribute == 'nailyarkk@ya.ru'

    @pytest.mark.usefixtures("driver", "wait")
    def test_signin_form_reg(self, driver, wait):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*SignInMain.SUBMIT_LOGIN).click()
        driver.find_element(*SignInMain.NAME_INPUT).send_keys(*SignInMain.name_const)
        driver.find_element(*SignInMain.PASSWORD_INPUT).send_keys(*SignInMain.password_const)
        driver.find_element(*SignInMain.SUBMIT_BUTTON_SIGN_IN).click()
        driver.find_element(*SignInMain.SUBMIT_LK).click()
        wait.until(EC.invisibility_of_element_located(*SignInMain.element_modal))

        element = wait.until(EC.presence_of_element_located(*SignInMain.element_value))

        name = driver.find_element(*SignInMain.CURR_NAME)
        value_attribute = name.get_attribute('value')

        assert value_attribute == 'nailyarkk@ya.ru'

    @pytest.mark.usefixtures("driver", "wait")
    def test_signin_form_resetpass(self, driver, wait):
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*SignInMain.SUBMIT_LOGIN).click()
        driver.find_element(*SignInMain.NAME_INPUT).send_keys(*SignInMain.name_const)
        driver.find_element(*SignInMain.PASSWORD_INPUT).send_keys(*SignInMain.password_const)
        driver.find_element(*SignInMain.SUBMIT_BUTTON_SIGN_IN).click()

        driver.find_element(*SignInMain.SUBMIT_LK).click()
        wait.until(EC.invisibility_of_element_located(*SignInMain.element_modal))

        element = wait.until(EC.presence_of_element_located(*SignInMain.element_value))

        name = driver.find_element(*SignInMain.CURR_NAME)
        value_attribute = name.get_attribute('value')

        assert value_attribute == 'nailyarkk@ya.ru'
