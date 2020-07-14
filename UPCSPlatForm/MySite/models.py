# auth:zbk,lby
# create date:7.10
# description:

from django.db import models


class User(models.Model):

    UserID = models.CharField(max_length=128,unique=True)
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


class Evaluation(models.Model):    
    EvaluationID = models.CharField(max_length=128,unique=True)
    UserID = models.CharField(max_length=128)
    Description = models.CharField(max_length=256)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.EvaluationID

    class Meta:
        ordering = ["EvaluationID","Date"]
        verbose_name = "用户评价"
        verbose_name_plural = "用户评价"

