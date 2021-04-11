import requests


url = 'http://127.0.0.1:8080/api/'

def check_users(username='', department=''):
    response = requests.get(url + 'users/' + f'?username={username}&department={department}').text
    return response

def check_department(department=''):
    response = requests.get(url + 'department/' + department).text
    return response    
