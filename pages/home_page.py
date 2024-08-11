import pytest
from pages.constants.home_page_constants import *
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
    
    def click_submit_button(self):
        submit_button = self.wait_element_visibility(SUBMIT_BUTTON)
        submit_button.click()
