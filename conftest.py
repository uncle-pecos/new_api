import pytest
import sys
import json
from api_check import check_users
from final_project import Userss, Departments
import cherrypy

@pytest.fixture()
def start_api():
    try:
        with open('database.json', encoding='utf-8') as f:
            users = json.load(f)

    except:
        print('You need database.json')    
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

    cherrypy.quickstart()
    cherrypy.engine.stop()
    yield
    
    sys.exit()