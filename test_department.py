import pytest
import requests
import json

try:
    with open('database.json', encoding='utf-8') as f:
        users = json.load(f)

except:
    print('You need database.json')

response1 = requests.get('http://127.0.0.1:8080/api/department/').text

print(response1)


