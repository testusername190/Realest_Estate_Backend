# Creating the Base Image
FROM python:3.10.6-alpine3.15

# setup environment variable  
ENV DockerHOME=/app

# set work directory  
RUN mkdir -p $DockerHOME 

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies mysqlclient using mariadb connector and delete it after installation. 
RUN apk update && \
    apk add --no-cache mariadb-connector-c-dev && \
    apk add --no-cache python3 python3-dev mariadb-dev build-base && \
    pip3 install --no-cache-dir mysqlclient && \
    apk del python3-dev mariadb-dev build-base

# checking the network adapters inside the docker container
RUN apk add netcat-openbsd

# copy whole project to your docker app directory. 
COPY ./backend $DockerHOME  

# run this command to install all dependencies  
RUN pip3 install --no-cache-dir django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow 

# we create a new wait.sh file who makes our django app wait for the db to startup.
COPY wait.sh /wait.sh
RUN chmod +x /wait.sh


