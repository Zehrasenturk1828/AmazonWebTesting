import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.constants.search_result_constants import *


@pytest.fixture(scope="function")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") 
    chrome_options.add_argument("--disable-extensions") 
    chrome_options.add_argument("--disable-plugins-discovery") 
    chrome_options.add_argument("--disable-popup-blocking") 
    chrome_options.add_argument("--disable-save-password-bubble") 
    chrome_options.add_argument("--disable-translate") 
    chrome_options.add_argument("--disable-notifications") 
    chrome_options.add_argument("--disable-default-apps") 
    chrome_options.add_argument("--disable-infobars") 
    driver = webdriver.Chrome(chrome_options)
    
    BASE_URL = "http://www.amazon.com.tr"
    driver.get(BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()