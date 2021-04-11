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
    pass

    yield   

    with open('tests.log') as fl:
        for line in fl:
            print(line)
    #os.remove('tests.log')
    while True:
        pass
