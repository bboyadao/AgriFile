#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createcachetable
echo "startting appication"
gunicorn -b 0.0.0.0 -p 9000 AgriFile.wsgi:application
