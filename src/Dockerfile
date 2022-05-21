FROM python:3.9

WORKDIR /usr/src/app

COPY ./flask/requirements.txt /root/

ENV FLASK_APP=app

RUN pip install --upgrade pip
RUN pip install -r ~/requirements.txt