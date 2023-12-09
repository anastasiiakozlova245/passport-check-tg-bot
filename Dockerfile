FROM docker.io/python:3.10-alpine3.19

USER root
COPY . .

RUN pip3 install telebot

ENTRYPOINT ["python3", "scripts/main.py"]