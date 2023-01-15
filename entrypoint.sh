#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createcachetable
echo "startting appication"
gunicorn --bind 0.0.0.0:9000 --workers 3 AgriFile.wsgi:application
