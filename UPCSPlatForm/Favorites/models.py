# auth:lby
# create date:7.21
# description: 收藏数据表

from win32timezone import now
from CoursePart import views as Course_Views
from django.db import models
from CoursePart.models import Course
from MySite.models import User

class Favorites(models.Model):
    ID = models.AutoField(primary_key=True)
    Course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Create_Date = models.DateTimeField(null=False, default=now)

    def __str__(self):
        return "%s likes course %s" %(self.User_ID,Course_Views.query_by_id2(self.Course_ID))
    
    class Meta:
        ordering = ['ID','Create_Date']
        unique_together = ('Course_ID','User_ID')
        verbose_name = '收藏'
        verbose_name_plural = '收藏'
