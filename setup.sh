#!/bin/bash

pip install --upgrade pip

pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic


python manage.py shell <<EOF
from django.contrib.auth.models import User

# Check if the superuser already exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'calebmwema65@gmail.com', '12admin!@')
EOF
