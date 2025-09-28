#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p backend/staticfiles

cd backend

# Try to run collectstatic, but continue if it fails
python manage.py collectstatic --noinput --clear || echo "Static collection failed, continuing..."

# Run migrations
python manage.py migrate

# Create superuser automatically (only if it doesn't exist)
echo "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings')
import django
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='thaboadmin').exists():
    User.objects.create_superuser('thaboadmin', 'admin@thabo.com', 'ThaboMedical2024!')
    print('✓ Superuser thaboadmin created successfully')
else:
    print('✓ Superuser thaboadmin already exists')

if not User.objects.filter(username='thabo').exists():
    User.objects.create_superuser('thabo', 'thabo@gmail.com', 'ThaboMedical2024!')
    print('✓ Superuser thabo created successfully')
else:
    print('✓ Superuser thabo already exists')
" | python manage.py shell

cd ..
