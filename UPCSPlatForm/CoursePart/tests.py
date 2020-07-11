from django.test import TestCase
from CoursePart import models
from CoursePart import views

# Begin
# auth:gz
# create date:7.11
# description:课程部分测试代码
# Create your tests here.


class testCoursePart:

    def test_add_course(self):
        views.add_course('2019020101', '软工实训',
                         '专业必修', '刘兆生',
                         '计算机学院', 2.0,
                         '2020.07')
        assert views.query_by_id('2019020101') is not None

# End
