import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from locators import SignInMain
from constants import *


class TestConstructor:
    def wait(self, driver):
        return WebDriverWait(driver, 10)

    def constructor(self, driver, tab_name, tab_loc_name):
        tab_element = driver.find_element(*tab_name)

        try:
            if tab_element.is_enabled():
                tab_element.click()
            else:
                print(f"некликабельный")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        element = driver.find_element(*SignInMain.constrfindtab)

        actual_text = element.text
        expected_text = tab_loc_name

        assert actual_text == expected_text

    @pytest.mark.parametrize("tab, tab_loc_name", [
        (SignInMain.sousy, "Соусы"),
        (SignInMain.nachinky, "Начинки"),
        (SignInMain.bulky, "Булки")
        ,
    ])
    def test_constructor_tab(self, driver, auth, tab, tab_loc_name):
        auth(name_site, SignInMain.SUBMIT_BUTTON)
        self.constructor(driver, tab, tab_loc_name)
