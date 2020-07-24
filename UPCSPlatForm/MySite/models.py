# auth:zbk,lby
# create date:7.10
# description:

from django.db import models


class User(models.Model):
    UserID = models.CharField(max_length=128, unique=True)
    UserName = models.CharField(max_length=128)
    Password = models.CharField(max_length=256)
    Email = models.EmailField(unique=True)
    JoinDate = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.UserID

    class Meta:
        ordering = ["-JoinDate"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    JoinDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.UserName + ":   " + self.code

    class Meta:
        ordering = ["-JoinDate"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"

# End
