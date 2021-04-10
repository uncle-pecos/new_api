FROM frolvlad/alpine-python3

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

ADD final_project.py /server/
ADD database.json /server/
WORKDIR /server/
ENTRYPOINT ["python3", "final_project.py"]