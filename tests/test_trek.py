from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from helpers import generate_random_login, generate_random_password, generate_random_name

class TestRegistration:
    @pytest.mark.usefixtures("driver", "wait")
    def test_registration(self, driver, wait):
        driver.get(*RegistrationPageLocators.reg_site)

        random_login = generate_random_login()
        random_password = generate_random_password()
        random_name = generate_random_name()

        name_field = driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        email_field = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        password_field = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)

        name_field.send_keys(random_name)
        email_field.send_keys(random_login)
        password_field.send_keys(random_password)

        before_url = driver.current_url

        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_changes(before_url))
        after_url = driver.current_url

        assert after_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()
