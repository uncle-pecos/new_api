docker build -t api-tests .
docker run -d -p 8080:8080 api-tests
