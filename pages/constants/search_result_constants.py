from selenium.webdriver.common.by import By

SEARCHRESULT_TITLE = (By.XPATH,"//*[@id='search']/span[2]/div/h1/div/div[1]/div/div/span[3]")
PAGINATION_BUTTON_2 = (By.CSS_SELECTOR, "[aria-label='2 sayfasına git']")
SELECTED_PAGINATION_2 = (By.XPATH, "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[66]/div/div/span/span[1]")
FIND_PRODUCT = (By.XPATH, "//div[@data-component-type='s-search-result']:nth-child(21)")
SPONSORED_LOC = (By.XPATH,"//div[@data-asin][10]")

