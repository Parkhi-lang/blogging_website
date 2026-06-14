#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "
from django.contrib.auth.models import User
print('All users:', list(User.objects.values('username', 'is_staff', 'is_superuser')))
u, created = User.objects.get_or_create(username='admin')
u.set_password('admin1234')
u.is_staff = True
u.is_superuser = True
u.is_active = True
u.save()
print('Created:', created)
print('User saved:', u.username, u.is_staff, u.is_superuser, u.is_active)
"
