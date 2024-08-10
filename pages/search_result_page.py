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

    def click_a_product(self):
        try:
            spl = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(SPONSORED_LOC))
            print("Dinamik öğe bulundu")
            self.driver.execute_script("arguments[0].style.display = 'none';", spl)
            print("Dinamik öğe kaldırıldı")
        except TimeoutError:
            print("Dinamik öğe bulunamadı")
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                product = self.driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result'][21]")
                product.click()
                logging.info("Tıklama başarılı.")
                print("Tıklama başarılı.")
                break
            except Exception as e:
                logging.error(f"Tıklama başarısız, deneme {attempt+1}: {str(e)}")
                print(f"Tıklama başarısız, deneme {attempt+1}: {str(e)}")
                time.sleep(1)
