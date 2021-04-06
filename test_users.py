import pytest
import sys
import json
from api_check import check_users
from final_project import Userss, Departments
import cherrypy


try:
    with open('database.json', encoding='utf-8') as f:
        users = json.load(f)

except:
    print('You need database.json')



def test_empty():  
    assert check_users() == str(users)

def test_plus_dep():
    temp = {}
    for i in users:
        if users[i]['department'] == 'FRS':
            temp[i] = users[i]
    assert check_users(department='FRS') == str(temp)

def test_plus_dep_name():
    temp = {}
    for i in users:
        if 'o' in users[i]['username']:
            temp[i] = users[i]
        if users[i]['department'] != 'FT':
            try:
                del temp[i]
            except:
                pass
    assert check_users(department='FT', username = 'o') == str(temp)

def test_plus_name():
    temp = {}
    for i in users:
        if 'o' in users[i]['username']:
            temp[i] = users[i]
    assert check_users(username = 'o') == str(temp)



print(str(check_users('?department=FRS')))

