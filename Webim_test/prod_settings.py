from pathlib import Path

import confidential_data


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = confidential_data.secret_key()

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Webim_test.data',
        'USER': 'postgres',
        'PASSWORD': confidential_data.pgsql_pass(),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}