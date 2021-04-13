import pytest
import json


@pytest.fixture(scope="module")
def start_db():
    print('\nDatabase connected\n')
    database_op = open('database.json', encoding='utf-8')             #  connect to our database
    database = json.load(database_op)                                 #  parse our database  
    deps = []
    for user in database:
        if database[user]['department'] not in deps:
            deps.append(database[user]['department'])
    test_list = list(database.keys())[1]
    user = {test_list : database[test_list]}
    ress = deps[0]

    yield database, user, ress, deps, test_list, database_op

    database_op.close()                                        # close database connection
    print('\nDatabase disconnected')
    # with open('tests.log') as fl:
    #     for line in fl:
    #         print(line)
            

