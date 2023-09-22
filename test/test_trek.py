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


class TestTrek:
    def trekfromLKtoConstr(self, driver):
        driver.find_element(*SignInMain.SUBMIT_LK).click()

        url_before_click = driver.current_url
        driver.find_element(*SignInMain.SUBMIT_CONSTRUCTOR).click()
        url_after_click = driver.current_url

        assert (not url_before_click == url_after_click)  and  url_after_click == name_site

    def test_trek(self, driver, auth):
        auth(name_site, SignInMain.SUBMIT_BUTTON)
        self.trekfromLKtoConstr(driver)
