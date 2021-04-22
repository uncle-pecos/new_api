A basic api using the
[CherryPy](http://cherrypy.org/) framework and Python 3.9.2.

The image is quite light thanks to
[Alpine Linux](https://hub.docker.com/r/frolvlad/alpine-python3/).


Run it
======

Run it from project main dir ('new_api'):

```
$ docker-compose up --build
```

Tests will start automatically

You can point your browser to http://locahost:8080/api/users/

There are database of users:
- id
- username
- email
- department
- data_joined

Endpoints:
- /api/users/
- /api/department/

You can check all users by http://locahost:8080/api/users/
Also it has filters by 'username' and 'department' (case sensitive) 

You can check all departments by http://locahost:8080/api/department/
Also it has filter by 'department' (case sensitive) 

Finally you can stop the server (from project main dir):

```
$ docker-compose down
```


Build it and run
========

You may rebuild the server image from 'server' dir:

```
$ docker build -t api-start .
$ docker run -d -p 8080:8080 api-start
```


If you use Windows you may run start_api.bat in server dir.

Run tests
========

You may build and run tests (client part) from 'client' dir:

```
$ docker build -t api-tests .
$ docker run -d -p 8080:8080 api-tests
```


Show logs
========

To show logs open client CLI and use:

```
$ cat tests.log
```
