from django.contrib import admin
from django.contrib.admin import site
from .models import *
from .tasks import *
from moonsheep.register import base_task

# Register your models here.

# # Register model to see it in the /admin panel
# site.register(Person)
#
# # If you want to customize admin functionality then you can define it in a separate class
# # Read more about it at https://docs.djangoproject.com/en/dev/ref/contrib/admin/#modeladmin-objects
# @admin.register(Politician, site=site)
# class PoliticianAdmin(admin.ModelAdmin):
#     pass
#

# On Linux run following command to generate register lines
# cat models.py | grep class | cut -d \  -f 2 | cut -d \( -f 1 | awk '{print "site.register(" $0 ")"}'

base_task.register(TaskWithForm)
base_task.register(TaskWithTemplate)
