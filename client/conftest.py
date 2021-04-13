import pytest
import json


@pytest.fixture(scope="module")
def start_db():
    
    def _method():
        database = json.load(open('database.json', encoding='utf-8'))
        print('Database connected')

        deps = []

        for user in database:
            if database[user]['department'] not in deps:
                deps.append(database[user]['department'])
        test_list = list(database.keys())[1]
        user = {test_list : database[test_list]}
        ress = deps[0]

        return database, user, ress, deps, test_list

    
    yield _method

    def _method(database):  
        database.close()
    with open('tests.log') as fl:
        for line in fl:
            print(line)
            return _method

