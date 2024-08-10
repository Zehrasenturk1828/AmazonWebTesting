import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.constants.home_page_constants import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

@pytest.mark.usefixtures("setup")

class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    def click_cookies(self):
        cookies_button = self.wait_element_visibility(COOKIES_BUTTON)
        cookies_button.click()
        
    def search_product(self):
        searchbox = self.wait_element_visibility(SEARCHBOX)
        searchbox.send_keys(SEARCH_PRODUCT_NAME)
        time.sleep(2)
    
    def click_submit_button(self):
        submit_button = self.wait_element_visibility(SUBMIT_BUTTON)
        submit_button.click()
        time.sleep(2)
