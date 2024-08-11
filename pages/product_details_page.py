import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.constants.product_details_constants import *
from pages.base_page import BasePage

@pytest.mark.usefixtures("setup")

class ProductDetailsPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def verify_product_details_page(self):
        title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PRODUCT_TITLE))
        return title.text
    
    def click_submit_button_to_cart(self):
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SUMBIT_BUTTON_TO_CART))
        submit_button.click()

    def click_go_to_basket_button(self):
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(TO_BASKET_BUTTON))
        submit_button.click()


        