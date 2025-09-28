import os
import sys

# Add the project root to Python path
sys.path.insert(0, '/home/harry/Desktop/project/amr_app/backend')

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings')

# Load environment variables
from dotenv import load_dotenv
load_dotenv('/home/harry/Desktop/project/amr_app/.env')

# Now import Django settings
import django
django.setup()

from django.conf import settings

print("=== Environment Test ===")
print("SECRET_KEY:", settings.SECRET_KEY)
print("DEBUG:", settings.DEBUG)
print("ALLOWED_HOSTS:", settings.ALLOWED_HOSTS)
print("DATABASES configured:", 'default' in settings.DATABASES)
if 'default' in settings.DATABASES:
    print("DATABASE ENGINE:", settings.DATABASES['default'].get('ENGINE', 'Not set'))
