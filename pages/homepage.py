
import os
import dotenv
dotenv.load_dotenv()

Login = os.getenv('Login')
password = os.getenv('password')
host = os.getenv('host')


from selenium.webdriver.common.by import By



class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(host)

    def click_pokemon(self):
        email = self.driver.find_element(By.CSS_SELECTOR, value='#k_email')
        email.click()

    def click_email(self):
        email = self.driver.find_element(By.CSS_SELECTOR, value='#k_email')
        email.click()
        email.send_keys(Login)


    def click_imputpassword(self):
        imputpassword = self.driver.find_element(By.CSS_SELECTOR, value='#k_password')
        imputpassword.click()
        imputpassword.send_keys(password)

    def click_food(self):
        food = self.driver.find_element(By.CSS_SELECTOR, value='#root > div > div > section > div.style_1_popup_white_in.style_1_popup_white_in_auth > form > button')
        food.click()

    def check_id_is(self, id ):
        title_a = self.driver.find_element(By.CSS_SELECTOR, value='#root > div > header > nav > div.right_block > a.header_card_trainer.style_1_interactive_button_link > div.header_card_trainer_id > div.header_card_trainer_id_num')
        assert title_a.text == id



