from pathlib import Path
import os
from os import getenv #helps to actually get env variable
from os import path #helps set base directory to the .env file
import dotenv #helps using .env files
from django.core.management.utils import get_random_secret_key



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#Me doing env variables import for both dev and prod
dotenv_file = BASE_DIR / '.env'

#then we check if it is a file, load it if it is
if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('DJANGO_SECRET_KEY', get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
# Since env vars are strings, in development we set it to 'True'and compare it to 'True'
# so it evaluates to True. In production we don't set it so its 'False' and evaluates to False
DEBUG = getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'users',
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Zagreb'

USE_I18N = True

USE_TZ = True






# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#-----------------------------------------------CONFIGURATION FOR STATIC FILES----------------------------------

STATIC_URL = 'static/' #this refers to 'static' folder in the apps themselves
MEDIA_ROOT = os.path.join(BASE_DIR, 'my_media_root')
MEDIA_URL = '/my_media_url/'

#this setting refers to directories that hold static files which are not tied to a particular app
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]



CRISPY_TEMPLATE_PACK = 'bootstrap4'


#--------------------------------------------- DEFAULT AUTHENTICATION CUSTOMIZATION----------------------------

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'users:profile'


#-------------------------------------------- EMAIL SETTINGS ----------------------------------------------------#

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'goranhir@gmail.com'
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'goranhir@gmail.com'