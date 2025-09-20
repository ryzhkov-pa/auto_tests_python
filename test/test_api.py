import requests
import pytest
import os
import dotenv
dotenv.load_dotenv()


URL = os.getenv('URL')
TOKEN = os.getenv('TOKEN')
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = os.getenv('TRAINER_ID')





def test_status_code():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert responce.status_code == 200
    print(responce.status_code)

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json ()["data"][0]['trainer_name'] == 'Кот'


