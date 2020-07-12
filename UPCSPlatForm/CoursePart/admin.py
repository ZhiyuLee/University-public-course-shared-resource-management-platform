from django.contrib import admin

# Register your models here.


# Begin
# auth:gz
# create date:7.11
# description:管理课程


from . import models

admin.site.register(models.Course)

# End
