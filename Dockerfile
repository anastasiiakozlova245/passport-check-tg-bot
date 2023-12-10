FROM docker.io/python:3.10-alpine3.19

USER root
COPY . .

RUN apk update && apk add curl
RUN pip3 install telebot

ENTRYPOINT ["python3", "scripts/main.py"]