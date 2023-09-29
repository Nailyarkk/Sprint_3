import pytest
from selenium import webdriver
from locators import SignInMain
from constants import *

class TestSignOut:
    def test_signout(self, driver, auth):
        auth(name_site, SignInMain.SUBMIT_BUTTON)

        driver.find_element(*SignInMain.SUBMIT_LK).click()
        driver.find_element(*SignInMain.SUBMIT_EXIT).click()

        url_before_click = driver.current_url
        driver.find_element(*SignInMain.SUBMIT_LK).click()
        url_after_click = driver.current_url

        assert url_before_click == url_after_click
