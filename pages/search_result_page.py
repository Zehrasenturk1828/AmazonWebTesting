import time
import pytest
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.constants.search_result_constants import *
from pages.base_page import BasePage

@pytest.mark.usefixtures("setup")

class SearchResultPage(BasePage):
    FIND_PRODUCT = (By.CSS_SELECTOR, 'div .a-size-base-plus.a-color-base.a-text-normal')
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def verify_result_page(self):
        title = self.wait_element_presence(SEARCHRESULT_TITLE)
        return title.text
    
    def click_second_page(self):
        second_page = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(PAGINATION_BUTTON_2))
        second_page.click()


    def verify_page_number(self):
        nav_button = self.wait_element_visibility(PAGINATION_BUTTON_2)
        return nav_button.text

    def click_a_product(self, index):
        products = self.find_elements(self.FIND_PRODUCT)
        if products:
            index_to_click = min(index, len(products) - 1)
            products[index_to_click].click()
        else:
            raise Exception("No products found on the search results page.")
