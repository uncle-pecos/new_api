import pytest
import sys
import json
from api_check import check_users
from api_check import check_department
from final_project import Userss, Departments
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


c = 0
request_users = 'users/'
request_dep = 'department/'
res_good = 'PASSED'
res_bad = 'FAILED'

def logging(result, i, request, response):
    url = "http://127.0.0.1:8080/api/"
    with open('tests.log', 'a+', encoding='utf-8') as fl:
        line = f'test{i}:\n{url}{request}                  {result}\n'
        fl.writelines(line)
        line = f'{response}\n\n'
        fl.writelines(line)

def test_empty():
    global c
    c += 1
    res = check_users()
    if res == str(users):
        logging(res_good, c, request_users, res)
    else:
        logging(res_bad, c, request_users, res)  
    assert res == str(users)

def test_empty_dep_plus_name():
    global c
    for user in users:
        name = name = name = users[user]['username']
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

def test_empty_dep_wrong_name():
    global c
    for user in users:
        name = name = users[user]['username']
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

def test_empty_name_plus_dep():
    global c
    for user in users:
        name = users[user]['department']
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

def test_empty_name_plus_wrong_dep():
    global c
    for user in users:
        name = users[user]['department']
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

def test_plus_dep():
    global c
    for user in users:
        name = users[user]['department']
        c += 1
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

def test_plus_wrong_dep():
    global c    
    for user in users:
        c += 1
        name = users[user]['department'] 
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

def test_plus_dep_name():
    global c
    for user in users:
        c += 1
        name = users[user]['department'] 
        name1 = users[user]['username']
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

def test_wrong_dep_name():
    global c    
    for user in users:
        c += 1
        name = users[user]['department'] 
        name1 = users[user]['username']    
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

def test_plus_part_name():
    global c
    for user in users:
        c += 1
        name = users[user]['username'][0]
        name1 = users[user]['username'][1] 
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

def test_plus_wrong_name():
    global c   
    for user in users:
        c += 1
        name = users[user]['username']
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

def test_plus_fullname():
    global c   
    for user in users:
        c += 1
        name = users[user]['username']
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

def test_empty_dep():
    global c
    c += 1
    res = check_department()    
    req = request_dep
    if res == str(deps):
        logging(res_good, c, req, res)
    else:
        logging(res_bad, c, req, res) 
    assert res == str(deps)

def test_part_dep():
    global c
    s = []
    for ress in deps:
        if len(ress) < 2:
            if ress[0] not in s:
                s.append(ress[0])
        else:
            if ress[0] + ress[1] not in s:
                s.append(ress[0] + ress[1])
            if ress[0] not in s:
                s.append(ress[0])
         
    for part in s:
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

def test_wrong_dep():
    global c
    for ress in deps:
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

def test_full_dep():
    global c    
    for ress in deps:
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

