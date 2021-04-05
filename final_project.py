import cherrypy
import json

try:
    with open('database.json', encoding='utf-8') as f:
        users = json.load(f)

except:
    print('You need database.json')



class Userss:
    global users
    def GET(self, username=None, department=None):
        data1 = []

        if username == None:
            for user in users:
                if users[user]['username'] not in data1:
                    data1.append(users[user]['username'])   
        else:
            for user in users:
                if username == users[user]['username'] or username in users[user]['username']:
                        if users[user]['username'] not in data1:
                            data1.append(users[user]['username']) 

        if department != None:
            for user in users:
                if department != users[user]['department']:
                    try:
                        data1.remove(users[user]['username'])  
                    except:
                        pass   

        return {'data: %s' % data1}

    def POST(self, a, b):
        return a

    exposed = True

class Departments:

    def GET(self, department=None):
        #data1 = {}
        data1 = []
        if department == None:
            for depart in users:
                #data1[depart] = users[depart]
                if users[depart]['department'] not in data1:
                    data1.append(users[depart]['department'])  
        else:
            for depart in users:
                if department == users[depart]['department'] or department in users[depart]['department']:
                    if users[depart]['department'] not in data1:
                        data1.append(users[depart]['department'])  
                    #data1[depart] = users[depart] 

        return {'data: %s' % data1}

    exposed = True

if __name__ == '__main__':
    cherrypy.tree.mount(
        Userss(), '/api/users', {
            '/': 
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.tree.mount(
        Departments(), '/api/department', {
            '/': 
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )    

    cherrypy.engine.start()
    cherrypy.engine.block()