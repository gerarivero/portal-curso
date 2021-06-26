#!/bin/sh

python manage.py makemigrations portal

python manage.py migrate --noinput