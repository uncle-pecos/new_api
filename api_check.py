import requests
import json

try:
    with open('database.json', encoding='utf-8') as f:
        users = json.load(f)

except:
    print('You need database.json')



url = 'http://127.0.0.1:8080/api/'

def check_users(username='', department=''):
    response = requests.get(url + 'users/' + f'?username={username}&department={department}').text
    return response

def check_department(params=''):
    response = requests.get(url + 'department/' + params).text
    return response    


# if check_users() == str(users):
#     print('ok')

#response1 = requests.get('http://127.0.0.1:8080/api/users/').text
# response2 = requests.get('http://127.0.0.1:8080/api/users/?department=FT').text
# response3 = requests.get('http://127.0.0.1:8080/api/users/?department=FRS&username=ivan').text
# response4 = requests.get('http://127.0.0.1:8080/api/users/1').text