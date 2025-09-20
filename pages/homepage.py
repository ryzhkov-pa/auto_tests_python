import json
import os
import dotenv
dotenv.load_dotenv()

login = os.getenv('Login')
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
        email.send_keys(login)


    def click_input_password(self):
        input_password = self.driver.find_element(By.CSS_SELECTOR, value='#k_password')
        input_password.click()
        input_password.send_keys(password)

    def click_food(self):
        food = self.driver.find_element(By.CSS_SELECTOR, value='#root > div > div > section > div.style_1_popup_white_in.style_1_popup_white_in_auth > form > button')
        food.click()

    def check_id_is(self, id ):
        title_a = self.driver.find_element(By.CSS_SELECTOR, value='#root > div > header > nav > div.right_block > a.header_card_trainer.style_1_interactive_button_link > div.header_card_trainer_id > div.header_card_trainer_id_num')
        assert title_a.text == id



