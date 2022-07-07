#!/bin/sh

set -e

python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4  --master --enabke-threads --module app.uwsgi
