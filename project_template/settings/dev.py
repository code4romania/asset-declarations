"""
Django settings for project_template project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

from .base import *

"""
If set Moonsheep won't communicate with PyBossa and will:
1. serve random mocked tasks
2. send form submissions straight to the verification
   won't test cross-checking as there is going to be only one entry, but will allow to test the whole flow
"""

DEBUG = TEMPLATE_DEBUG = True

MOONSHEEP["DEV_ROTATE_TASKS"] = True

INTERNAL_IPS = ["127.0.0.1", "localhost"]

AUTH_PASSWORD_VALIDATORS = []

MOONSHEEP_BASE_TASKS = [
    "project-template.tasks.TaskWithForm",
    "project-template.tasks.TaskWithTemplate",
]

# Add debug toolbar
if DEBUG:
    INSTALLED_APPS += ["debug_toolbar", "django_extensions"]
    MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")

# TODO: read it from env or generate a new one
SECRET_KEY = "https://uploads.skyhighnetworks.com/wp-content/uploads/2015/08/06195203/Bart-Chalkboard-for-Blog-Post.png"

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
