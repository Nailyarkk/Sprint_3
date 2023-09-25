import pytest
from selenium import webdriver
from locators import SignInMain
from constants import *

class TestConstructor:
    @pytest.mark.parametrize("tab", [
        (SignInMain.sousy),
        (SignInMain.nachinky),
        (SignInMain.bulky)
    ])
    def test_constructor_tab(self, driver, auth, tab):
        auth(name_site, SignInMain.SUBMIT_BUTTON)
        shag1 = driver.find_element(tab)

        shag1.click()

        shag2 = shag1.get_attribute('class')

        assert shag2 == active_tab_class