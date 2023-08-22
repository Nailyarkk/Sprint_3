import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from locators import SignInMain

class TestConstructor:
    @pytest.mark.usefixtures("driver", "wait")
    def test_sousy(self, driver, wait):
        driver.get(*SignInMain.name_site)
        driver.find_element(*SignInMain.SUBMIT_BUTTON).click()
        driver.find_element(*SignInMain.NAME_INPUT).send_keys(*SignInMain.name_const)
        driver.find_element(*SignInMain.PASSWORD_INPUT).send_keys(*SignInMain.password_const)
        driver.find_element(*SignInMain.SUBMIT_BUTTON_SIGN_IN).click()
        sousy_element = driver.find_element(*SignInMain.sousy)
        sousy_element.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(*SignInMain.tab_type_current_locator_sousy)
        )
        tab_type_current_element = driver.find_element(*SignInMain.tab_type_current_locator_sousy)
        assert "tab_tab_type_current__2BEPc" in tab_type_current_element.get_attribute("class")

    @pytest.mark.usefixtures("driver", "wait")
    def test_nachinky(self, driver, wait):
        driver.get(*SignInMain.name_site)

        driver.find_element(*SignInMain.SUBMIT_BUTTON).click()
        driver.find_element(*SignInMain.NAME_INPUT).send_keys(*SignInMain.name_const)
        driver.find_element(*SignInMain.PASSWORD_INPUT).send_keys(*SignInMain.password_const)
        driver.find_element(*SignInMain.SUBMIT_BUTTON_SIGN_IN).click()
        nachinky_element = driver.find_element(*SignInMain.nachinky)
        nachinky_element.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(*SignInMain.tab_type_current_locator_nachinky)
        )
        tab_type_current_element = driver.find_element(*SignInMain.tab_type_current_locator_nachinky)
        assert "tab_tab_type_current__2BEPc" in tab_type_current_element.get_attribute("class")

    @pytest.mark.usefixtures("driver", "wait")
    def test_bulky(self, driver, wait):
        driver.get(*SignInMain.name_site)

        driver.find_element(*SignInMain.SUBMIT_BUTTON).click()
        driver.find_element(*SignInMain.NAME_INPUT).send_keys(*SignInMain.name_const)
        driver.find_element(*SignInMain.PASSWORD_INPUT).send_keys(*SignInMain.password_const)
        driver.find_element(*SignInMain.SUBMIT_BUTTON_SIGN_IN).click()
        bulky_element = driver.find_element(*SignInMain.bulky)
        bulky_element.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(*SignInMain.tab_type_current_locator_bulky)
        )
        tab_type_current_element = driver.find_element(*SignInMain.tab_type_current_locator_bulky)
        assert "tab_tab_type_current__2BEPc" in tab_type_current_element.get_attribute("class")

