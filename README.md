# project-template
Project template for Code4Romania Moonsheep implementation.
Starting from this templates, additional tasks can be added in tasks.py to be run by the platform.

How to start-up this Moonsheep project (you need python3 for this):

1. Clone this repo
2. Cd to the folder where you have cloned this repo
3. pip/pip3 install -r requirements-dev.txt
4. export DJANGO_SETTINGS_MODULE=project_template.settings.dev
5. python/python3 manage.py migrate
6. python/python3 manage.py runserver

After doing the above steps, you should be able to see the server running by accessing localhost:8000 in your browser and seeing the inital dummy tasks.
