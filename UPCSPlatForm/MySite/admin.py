
#auth:zbk
#create date:7.11
#description:

from django.contrib import admin


from . import models

admin.site.register(models.User)
admin.site.register(models.ConfirmString)

