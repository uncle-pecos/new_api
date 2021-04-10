import cherrypy
import json
import sys

try:
    with open('database.json', encoding='utf-8') as f:
        users = json.load(f)

except:
    print('You need database.json')


# class Main:
#     def starts_api(self):
class Userss:

    def GET(self, username=None, department=None):
        data1 = {}

        if username == None and username != '':
            for user in users:
                if users[user]['username'] not in data1:
                    data1[user] = users[user]
        else:
            for user in users:
                if username == users[user]['username'] or username in users[user]['username']:
                        if user not in data1:
                            data1[user] = users[user]  

            # print(data1, '+++', department)

        if department != '' and department != None:
            for user in users:
                if department != users[user]['department']:
                    try:
                        del data1[user]
                    except:
                        pass  
        # elif department == '':
        #     pass 
        return {'%s' % data1}

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

        return {'%s' % data1}

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
    
        
# start = Main()
# start.starts_api()