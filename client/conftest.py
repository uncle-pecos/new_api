import pytest
import sys
import json
from api_check import check_users
import cherrypy
import logging
import os


def shutdown_server():
    cherrypy.engine.exit()
    cherrypy.engine.block()


@pytest.fixture(scope="module")
def start_api():
    database = open('database.json', encoding='utf-8')
    print('Database connected')

    yield   
    database.close()
    with open('tests.log') as fl:
        for line in fl:
            print(line)
    

