import os

# Read the current settings
with open('backend/amr_project/settings.py', 'r') as f:
    content = f.read()

# Add deployment configuration at the end
deployment_config = '''

# Deployment settings for Render
import dj_database_url
import os

# Database configuration for Neon
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# Security settings for production
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '.onrender.com,localhost,127.0.0.1').split(',')

# Static files configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Whitenoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "https://your-app.netlify.app",
    "http://localhost:3000",
]

# Use environment variable for secret key
SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
'''

# Append deployment config
with open('backend/amr_project/settings.py', 'a') as f:
    f.write(deployment_config)
