import pytest
import sys
import json
from api_check import check_users
from api_check import check_department
import cherrypy


try:
    with open('database.json', encoding='utf-8') as f:
        users = json.load(f)

except:
    print('You need database.json')

deps = []
for user in users:
    if users[user]['department'] not in deps:
        deps.append(users[user]['department'])

test_list = list(users.keys())[1]
user = {test_list : users[test_list]}        # test data for users
ress = deps[0]                              # test data for departments


c = 0
request_users = 'users/'
request_dep = 'department/'
res_good = '+++PASSED+++'
res_bad = '---FAILED---'


def logging(result, i, request, response):
    url = "http://127.0.0.1:8080/api/"
    with open('tests.log', 'a+', encoding='utf-8') as fl:
        line = f'test{i}:\n{url}{request}                  {result}\n'
        fl.writelines(line)
        line = f'{response}\n\n'
        fl.writelines(line)




def test_empty(start_api):
    global c
    c += 1
    res = check_users()
    if res == str(users):
        logging(res_good, c, request_users, res)
    else:
        logging(res_bad, c, request_users, res)  
    assert res == str(users)

def test_empty_dep_plus_name(start_api):
    global c
    name = user[test_list]['username']
    c += 1
    res = check_users(department='', username = name[0])
    req = request_users + f'?department=&username={name[0]}'
    temp = {}
    for i in users:
        if name[0] in users[i]['username']:
            temp[i] = users[i]
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)

def test_empty_dep_wrong_name(start_api):
    global c
    name = user[test_list]['username']
    c += 1
    res = check_users(department='', username = name + "0")
    req = request_users + f'?department=&username={name + "0"}'
    temp = {}
    for i in users:
        if name + "0" in users[i]['username']:
            temp[i] = users[i]
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)  

def test_empty_name_plus_dep(start_api):
    global c
    name = user[test_list]['department']
    c += 1
    res = check_users(department=name, username = '')
    req = request_users + f'?department={name}&username='
    temp = {}
    for i in users:
        if '' in users[i]['username']:
            temp[i] = users[i]
        if users[i]['department'] != name:
            try:
                del temp[i]
            except:
                pass
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)  

def test_empty_name_plus_wrong_dep(start_api):
    global c
    name = users[test_list]['department']
    c += 1
    res = check_users(department= name + '0', username = '')
    req = request_users + f'?department={name+"0"}&username='
    temp = {}
    for i in users:
        if '' in users[i]['username']:
            temp[i] = users[i]
        if users[i]['department'] != name + '0':
            try:
                del temp[i]
            except:
                pass
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)  

def test_plus_dep(start_api):
    global c
    c += 1
    name = users[test_list]['department']
    res = check_users(department=name)
    req = request_users + f'?department={name}'    
    temp = {}
    for i in users:
        if users[i]['department'] == name:
            temp[i] = users[i]
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)  

def test_plus_wrong_dep(start_api):
    global c    
    c += 1
    name = users[test_list]['department'] 
    res = check_users(department = name + '0')
    req = request_users + f'?department={name + "0"}'    
    temp = {}
    for i in users:
        if users[i]['department'] == name + '0':
            temp[i] = users[i]
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)  

def test_plus_dep_name(start_api):
    global c
    c += 1
    name = users[test_list]['department'] 
    name1 = users[test_list]['username']
    res = check_users(department=name, username = name1[0])
    req = request_users + f'?department={name}&username={name1[0]}' 
    temp = {}
    for i in users:
        if name1[0] in users[i]['username']:
            temp[i] = users[i]
        if users[i]['department'] != name:
            try:
                del temp[i]
            except:
                pass
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)

def test_wrong_dep_name(start_api):
    global c    
    c += 1
    name = users[test_list]['department'] 
    name1 = users[test_list]['username']    
    res = check_users(department = name + '0', username = name1 + '0')
    req = request_users + f'?department={name+"0"}&username={name1+"0"}' 
    temp = {}
    for i in users:
        if name1+"0" in users[i]['username']:
            temp[i] = users[i]
        if users[i]['department'] != name+"0":
            try:
                del temp[i]
            except:
                pass
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)    

def test_plus_part_name(start_api):
    global c
    c += 1
    name = users[test_list]['username'][0]
    name1 = users[test_list]['username'][1] 
    res = check_users(username = name)
    res1 = check_users(username = name + name1)
    req = request_users + f'username={name}'
    req1 = request_users + f'username={name + name1}' 
    temp = {}
    for i in users:
        if name in users[i]['username'] or name + name1 in users[i]['username']:
            temp[i] = users[i]
    if res == str(temp):
        logging(res_good, c, req, res)
        logging(res_good, c, req1, res1)
    else:
        logging(res_bad, c, req, res)
        logging(res_bad, c, req1, res1)  
    assert res == str(temp) 

def test_plus_wrong_name(start_api):
    global c   
    c += 1
    name = users[test_list]['username']
    res = check_users(username = name + '0')
    req = request_users + f'username={name + "0"}' 
    temp = {}
    for i in users:
        if name + '0' in users[i]['username']:
            temp[i] = users[i]
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)   

def test_plus_fullname(start_api):
    global c   
    c += 1
    name = users[test_list]['username']
    res = check_users(username = name)
    req = request_users + f'username={name}' 
    temp = {}
    for i in users:
        if name in users[i]['username']:
            temp[i] = users[i]
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)  

def test_empty_dep(start_api):
    global c
    c += 1
    res = check_department()    
    req = request_dep
    if res == str(deps):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(deps)

def test_part_dep(start_api):
    global c
    part = ress[0]
    c += 1
    res = check_department(department= part)    
    req = request_dep + f'?department={part}'
    temp = []
    for i in deps:
        if part in i:
            temp.append(i)
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)   

def test_wrong_dep(start_api):
    global c
    c += 1
    res = check_department(department= ress + '0')    
    req = request_dep + f'?department={ress + "0"}'
    temp = []
    for i in deps:
        if ress + '0' in i:
            temp.append(i)
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)   

def test_full_dep(start_api):
    global c        
    c += 1
    res = check_department(department= ress)    
    req = request_dep + f'?department={ress}'
    temp = []
    for i in deps:
        if ress in i:
            temp.append(i)
    if res == str(temp):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(temp)    

print('Please check "tests.log" for info about tests')

