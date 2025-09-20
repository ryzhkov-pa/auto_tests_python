from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_title_is(self, title ):
        page_title = self.driver.find_element(By.CSS_SELECTOR,value='#root > div > div > section > div.style_1_popup_white_in.style_1_popup_white_in_auth > h1')
        assert page_title.text == title

