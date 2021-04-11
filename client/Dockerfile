FROM frolvlad/alpine-python3

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

ADD . /client/

WORKDIR /client/


#RUN pytest -v -s test_all.py --disable-warnings
#RUN tail -f dev/null

