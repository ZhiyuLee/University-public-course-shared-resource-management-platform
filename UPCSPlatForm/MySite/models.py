from django.db import models

# Create your models here.

#Begin
#auth:zbk
#create date:7.10
#description:

class User(models.Model):

    UserID = models.CharField(max_length=128,unique=True)
    UserName = models.CharField(max_length=128)
    Password = models.CharField(max_length=256)
    Email = models.EmailField(unique=True)
    JoinDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.UserID

    class Meta:
        ordering = ["-JoinDate"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

#End