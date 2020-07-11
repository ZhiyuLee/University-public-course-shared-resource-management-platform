from django.contrib import admin

# Register your models here.

#Begin
#auth:zbk
#create date:7.11
#description:

from . import models

admin.site.register(models.User)
admin.site.register(models.ConfirmString)

#End