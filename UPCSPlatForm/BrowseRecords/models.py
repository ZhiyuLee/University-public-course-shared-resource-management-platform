# auth:lzy
# create date:7.22
# description:历史记录表


from django.db import models

# Create your models here.
from win32timezone import now
from CoursePart.models import Course
from MySite.models import User


class BrowseRecords(models.Model):
    RecordID = models.AutoField(primary_key=True)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)
    Time = models.DateTimeField(null=False, default=now)

    def __str__(self):
        return self.User_ID.UserName + ' ' + self.Time + ' ' + self.Course_ID.name

    class Meta:
        ordering = ["RecordID"]
        verbose_name = "浏览记录"
        verbose_name_plural = "浏览记录"
