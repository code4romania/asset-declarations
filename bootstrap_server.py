#!/usr/bin/env python

import os
import sys

DJANGO_ENV = 'DJANGO_SETTINGS_MODULE'

if __name__ == '__main__':

    # Check Python version
    pver = sys.version_info[0:3]
    if pver[0] < 3 or pver[1] < 4:
        print("The project requires Python 3.4 or greater. Current: {}.{}.{}".format(*pver))
        sys.exit(1)

    # Clean the migrations folder
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        mig_dir = os.path.join(dir_path, 'project_template/migrations')
        
        for file_ in os.listdir(mig_dir):
            file_path = os.path.join(mig_dir, file_)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            
            except Exception as e:
                print("Exception:", e)

    except FileNotFoundError:
        print("No migrations to clean.")
        
    # Remove SQLITE db
    try:
        os.unlink('db.sqlite3')
    except FileNotFoundError:
        print("No sqlite database to clean.")

    # Compile locales; has to be done before setting 'DJANGO_SETTINGS_MODULE' env
    if DJANGO_ENV in os.environ:
        del os.environ[DJANGO_ENV]
    
    for lang in ['en']:
        os.system('django-admin makemessages --locale {}'.format(lang))

    # Specify Django's settings module
    os.environ[DJANGO_ENV] = 'project_template.settings.dev'

    # Make migrations and run server
    for args in ['makemigrations', 'migrate --run-syncdb', 'runserver']:
        os.system('{} manage.py {}'.format(sys.executable, args))
    