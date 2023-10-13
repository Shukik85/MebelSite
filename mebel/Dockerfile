#########
# FINAL #
#########

# pull official base image
FROM python:3.11-alpine

# create the app user
RUN addgroup --system app
RUN adduser --ingroup app --disabled-password app

ENV APP_HOME=

# create directory for the app user
RUN mkdir -p /home/app
RUN mkdir /home/app/web
RUN mkdir /home/app/web/staticfiles
RUN mkdir /home/app/web/mediafiles
WORKDIR /home/app/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install system dependencies
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --upgrade netcat-openbsd

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# lint
RUN pip install flake8==6.0.0
RUN flake8 --ignore=E501,F401,F541 ./

# copy entrypoint.prod.sh
RUN sed -i 's/\r$//g'  /home/app/web/entrypoint.prod.sh
RUN chmod +x  /home/app/web/entrypoint.prod.sh

# chown all the files to the app user
RUN chown -R app:app /home/app/web

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]
