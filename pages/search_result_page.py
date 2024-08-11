import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.constants.search_result_constants import *
from pages.base_page import BasePage

@pytest.mark.usefixtures("setup")

class SearchResultPage(BasePage):
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
        nav_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(SELECTED_PAGINATION_2))
        return nav_button.text

    def click_a_product(self, index):
        products = self.find_elements(FIND_PRODUCT)
        if products:
            click_to_index = min(index, len(products) - 1)
            products[click_to_index].click()
        else:
            raise Exception("No products found on the search results page.")
