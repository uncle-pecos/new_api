FROM frolvlad/alpine-python3

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

ADD . /client/

WORKDIR /client/
