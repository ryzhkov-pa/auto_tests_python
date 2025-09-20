from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.product import ProductPage






def test_open (driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_pokemon()
    product_page = ProductPage(driver)
    product_page.check_title_is('Битва покемонов')

def test_autorization(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_email()
    homepage.click_imputpassword()
    homepage.click_food()
    homepage.check_id_is('17672')





