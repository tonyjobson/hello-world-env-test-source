FROM ubuntu

RUN apt-get update

RUN apt-get install -y python3 python3-pip python-dev

RUN pip3 install FLASK

COPY app.py /opt/app.py

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
