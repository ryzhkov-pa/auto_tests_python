import requests
import pytest
import os
import dotenv
dotenv.load_dotenv()
import json


URL = os.getenv('URL')
TOKEN = os.getenv('TOKEN')
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = os.getenv('TRAINER_ID')







def hyi():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    return json.loads(response.text), response.status_code

