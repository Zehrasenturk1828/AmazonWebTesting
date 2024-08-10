import time
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