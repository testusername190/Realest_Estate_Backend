#!/bin/sh

while ! nc -z mydb 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done


python3 manage.py makemigrations
python3 manage.py migrate

DJANGO_SUPERUSER_USERNAME=adminbrc DJANGO_SUPERUSER_EMAIL=adminbrc@example.com DJANGO_SUPERUSER_PASSWORD=password123 python3 manage.py createsuperuser --noinput --name admin


python3 manage.py runserver 0.0.0.0:8000
