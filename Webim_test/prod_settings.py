from pathlib import Path
import os

import confidential_data


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = confidential_data.secret_key()

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '194.67.108.112', 'xn------8cddhck7aht7bbcjcvebd0bq.xn--p1acf']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Webim_test.data',
        'USER': 'ilrootless',
        'PASSWORD': confidential_data.pgsql_pass(),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')