FROM python:3.11.5-alpine3.18

COPY requirements.txt /temp/requirements.txt

RUN pip install -U pip
RUN pip install -r /temp/requirements.txt

COPY mebel /mebel
WORKDIR /mebel
EXPOSE 8000

RUN apk update
RUN apk add postgresql-client build-base postgresql-dev

RUN adduser --disabled-password admin

USER admin
