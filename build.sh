#!/bin/bash
# Set environment variables for the build
export DATABASE_URL="postgresql://neondb_owner:npg_68AGChuOcZsB@ep-green-cloud-ad34rcz7-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

pip install -r requirements.txt

cd backend
python manage.py collectstatic --noinput
python manage.py migrate

# Create superuser automatically
echo "Creating superuser..."
echo "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='thaboadmin').exists():
    User.objects.create_superuser('thaboadmin', 'admin@thabo.com', 'ThaboMedical2024!')
    print('✓ Superuser created successfully')
else:
    print('✓ Superuser already exists')
" | python manage.py shell

cd ..
