#!/bin/bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
# Create superuser for admin access
echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('thaboadmin', 'admin@thabo.com', 'ThaboMedical2024!') if not User.objects.filter(username='thaboadmin').exists() else print('Superuser already exists')" | python manage.py shell
