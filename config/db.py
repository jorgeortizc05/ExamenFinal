import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'examen',
        'USER': 'jorge',
        'PASSWORD': 'jorge',
        'HOST': 'localhost',
        'DATABASE_PORT': '5432',
    }
}