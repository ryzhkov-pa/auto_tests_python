import pytest

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
    q = responce.status_code
    print(q)

