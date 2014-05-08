from settings import *

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3'
        # or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',
        # Or path to database file if sqlite3.
        'NAME': 'task_manager',
        # Not used with sqlite3.
        'USER': 'root',
        # Not used with sqlite3.
        'PASSWORD': 'temporal',
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '127.0.0.1',
        # Set to empty string for default. Not used with sqlite3.
        'PORT': 3306,
        # MySQLdb prior to creating your tables
        'OPTIONS': {'init_command': 'SET storage_engine=InnoDB'},
    }
}