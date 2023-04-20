# Creating the Base Image
FROM python:3.10.6

# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME 

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DB_HOST=host.docker.internal

# install dependencies  
RUN pip install --upgrade pip 
RUN apt-get update && apt-get install -y default-mysql-client


# copy whole project to your docker home directory. 
COPY . $DockerHOME  

# run this command to install all dependencies  
RUN pip install django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow 
RUN pip install mysqlclient

# port where the Django app runs  
EXPOSE 8000 

# start server  
CMD python manage.py runserver 