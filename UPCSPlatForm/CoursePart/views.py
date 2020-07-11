from django.shortcuts import render
from CoursePart import models, tests
import decimal

# Begin
# auth:gz
# create date:7.10
# description:课程部分操作


# Create your views here.
def index(request):
    # tests.testCoursePart.test_add_course(self=None)
    all_course = get_all_courses()
    return render(request, 'index.html', {'all_course': all_course})


def get_all_courses():
    return models.Course.objects.all()


def query_by_id(course_id):
    if course_id:
        try:
            course = models.Course.objects.get(ID=course_id)
        except:
            return None
        return course


def query_by_keyWord(keyWord):
    all_courses = get_all_courses()
    return all_courses.filter(name__contains=keyWord)


def query_by_type(course_type):
    return get_all_courses().filter(type=course_type)


def query_by_teacher(course_teacher):
    return get_all_courses().filter(teacherName__contains=course_teacher)


def delete_by_id(course_id):
    course = query_by_id(course_id)
    models.Course.delete(course)


# 课程号, 课程名, 课程类别, 授课教师, 授课学院, 课程学分, 学时安排
def add_course(course_id, course_name,
               course_type, course_teacher,
               course_collage, course_credit,
               course_time):
    new_course = models.Course()
    new_course.college = course_collage
    new_course.credit = course_credit
    new_course.ID = course_id
    new_course.name = course_name
    new_course.teacherName = course_teacher
    new_course.time = course_time
    new_course.type = course_type
    new_course.save()

# End
