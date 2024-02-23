#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py  collectstatic --noinput

# run this script only one time when creating the database for the first time to create a super user account
# echo "from django.contrib.auth import get_user_model; \
#  get_user_model().objects.create_superuser('${suseremail}', '${susername}', '${suserpassword}')" \
#  | python manage.py shell


exec uvicorn config.asgi:application --host 0.0.0.0 --reload --reload-include '*.html'
