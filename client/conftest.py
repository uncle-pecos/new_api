import pytest
import sys
import json
from api_check import check_users
from final_project import Userss, Departments
import cherrypy
import logging
import os


def shutdown_server():
    cherrypy.engine.exit()
    cherrypy.engine.block()


@pytest.fixture(scope="module")
def start_api():
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
    cherrypy.engine.wait(cherrypy.engine.states.STARTED)

    yield 
    
    shutdown_server()

    with open("tests.log") as file:
        for line in file:
            print(line)

    os.remove('tests.log')
