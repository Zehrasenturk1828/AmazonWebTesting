import time
import pytest
from pages.home_page import *
from pages.search_result_page import *
from pages.product_details_page import *
from tests.conftest import *
import softest

@pytest.mark.usefixtures("setup")
class TestCheckofProductAddtoBasket(softest.TestCase):
    def test_check_of_product_add_to_basket(self):
        home_page = HomePage(self.driver)
        home_page.click_cookies()
        self.assertEqual(HOME_PAGE_URL, home_page.get_URL(), "Amazon Anasayfa Açılmadı")
        home_page.search_product()
        home_page.click_submit_button()

        search_result_page = SearchResultPage(self.driver)
        search_result_page.verify_result_page()
        search_result_page.click_second_page()
        #self.assertEqual("2", search_result_page.verify_page_number(), "Beklenen sayfa eşleşmedi")
        time.sleep(2)
        search_result_page.click_a_product()

        # product_details_page = ProductDetailsPage(self.driver)
        # assert product_details_page.verify_product_details_page() is not None, "Ürün Detay sayfasında olunduğu doğrulandı"


