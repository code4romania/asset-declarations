"""
Django settings for project_template project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

from .base import *

# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# TODO: read secret env form env, it should be added at deploy time
SECRET_KEY = '${SECRET_KEY}'

# To be double sure
DEBUG = TEMPLATE_DEBUG = False
MOONSHEEP_DEVELOPMENT_MODE = True

ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = []

WSGI_APPLICATION = "project_template.wsgi.application"
