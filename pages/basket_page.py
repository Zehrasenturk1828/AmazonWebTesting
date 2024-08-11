import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.constants.basket_constants import *
from pages.base_page import BasePage

@pytest.mark.usefixtures("setup")

class BasketPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def verify_basket_page(self):
        basket_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(BASKET_TITLE))
        return basket_title.text

    def click_logo_to_homepage(self):
        logo = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LOGO))
        logo.click()