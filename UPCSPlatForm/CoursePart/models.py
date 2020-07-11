from django.db import models
import decimal

# Begin
# auth:gz
# create date:7.10
# description:课程数据库表实体类

# Create your models here.


class Course(models.Model):
    # 课程表

    type = (
        ('publicBasicCompulsory', '公共基础必修'),
        ('publicBasicElective', '公共基础选修'),
        ('generalEducationCompulsory', '通识教育必修'),
        ('generalEducationElective', '通识教育选修'),
        ('professionalEducationCompulsory', '专业教育必修'),
        ('professionalEducationElective', '专业教育选修'),
        ('publicCompulsory', '公共必修'),
        ('publicElective', '公共选修'),
        ('professionalCompulsory', '专业必修'),
        ('professionalElective', '专业选修'),
    )

    ID = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128, choices=type)
    teacherName = models.CharField(max_length=128)
    college = models.CharField(max_length=128)
    credit = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    time = models.CharField(max_length=128)
    # c_time = models.DateTimeField(auto_now_add=True)

    # 课程号, 课程名, 课程类别, 授课教师, 授课学院, 课程学分, 学时安排
    def __str__(self):
        return self.ID + ' ' + self.name + ' ' + \
               self.type + ' ' + self.teacherName + ' ' + \
               self.college + ' ' + str(self.credit) + ' ' + \
               self.time

    class Meta:
        ordering = ['ID']
        verbose_name = '课程'
        verbose_name_plural = '课程'

# End
