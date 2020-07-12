
# auth:gz
# create date:7.11
# description:管理课程

from django.contrib import admin
from . import models

admin.site.register(models.Course)

