import pytest


@pytest.fixture(scope="module")
def start_api():
    database = open('database.json', encoding='utf-8')
    print('Database connected')

    yield   
    database.close()
    with open('tests.log') as fl:
        for line in fl:
            print(line)
    

