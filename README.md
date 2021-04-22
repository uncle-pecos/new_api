A basic api using the
[CherryPy](http://cherrypy.org/) framework and Python 3.9.2.

The image is quite light thanks to
[Alpine Linux](https://hub.docker.com/r/frolvlad/alpine-python3/).


Run it
======

Run it from main project folder ('new_api'):

```
$ docker-compose up 
```

Tests will start automatically

You can point your browser to http://locahost:8080/

There are database of users:
- id
- username
- email
- department
- data_joined

Endpoints:
- /users/
- /department/

You can check all users by http://locahost:8080/users/
Also it has filters by 'username' and 'department'

You can check all departments by http://locahost:8080/department/
Also it has filter by 'department'

Finally you can stop the server (from main project folder):

```
$ docker-compose down
```


Build it and run
========

You may rebuild the server image from 'server' folder:

```
$ docker build -t api-start .
$ docker run -d -p 8080:8080 api-start
```

(it works in server folder)

If you use Windows you may run start_api.bat in server folder

Run tests
========

You may build and run tests (client part) from 'client' folder:

```
$ docker build -t api-tests .
$ docker run -d -p 8080:8080 api-tests
```

(it works in client folder)

Show logs
========

To show logs open client CLI and use:

```
$ cat tests.log
```
