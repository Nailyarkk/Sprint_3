from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import *
from locators import *
from constants import *


class TestRegistration:
    def test_registration(self, driver):
        driver.get(reg_site)

        random_login = generate_random_login()
        random_password = generate_random_password()
        random_name = generate_random_name()

        name_field = driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        email_field = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        password_field = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)

        name_field.send_keys(random_name)
        email_field.send_keys(random_login)
        password_field.send_keys(random_password)

        driver.find_element(*SignInMain.SUBMIT_LK).click()

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located(*SignInMain.CURR_NAME123))

        name = driver.find_element(*SignInMain.CURR_NAME123)
        value_attribute = name.get_attribute('value')

        assert value_attribute == random_name

