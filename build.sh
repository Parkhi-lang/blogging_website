
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "
from django.contrib.auth.models import User
u, created = User.objects.get_or_create(username='admin')
u.set_password('admin1234')
u.is_staff = True
u.is_superuser = True
u.save()
print('Done')
"
