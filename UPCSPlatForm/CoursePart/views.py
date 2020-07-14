# auth:gz
# create date:7.10
# description:课程部分操作

from django.shortcuts import render
from CoursePart import models, tests
import decimal
from django.shortcuts import render, redirect


def index(request):
    # tests.testCoursePart.test_add_course(self=None)
    flag_1 = flag_2 = flag_3 = True
    courses = get_all_courses()
    if request.GET.get('course_name') != "" and \
            request.GET.get('course_name') is not None:
        courses = web_query_by_name(courses, request)
        flag_1 = False
    if request.GET.get('course_id') != "" and \
            request.GET.get('course_id') is not None:
        flag_2 = False
        courses = web_query_by_id(courses, request)
    if request.GET.get('teacher_name') != "" and \
            request.GET.get('teacher_name') is not None:
        courses = web_query_by_teacher(courses, request)
        flag_3 = False
    if flag_1 and flag_2 and flag_3:
        # courses = get_all_courses()
        pass
    # all_course = get_all_courses()
    return render(request, 'index.html', {'courses': courses})


def get_all_courses():
    return models.Course.objects.all()


def query_by_id(courses, course_id):
    if course_id:
        try:
            course = courses.filter(ID=course_id)
        except:
            return None
        return course


def query_by_keyWord(courses, keyWord):
    # all_courses = get_all_courses()
    return courses.filter(name__contains=keyWord)


def query_by_type(courses, course_type):
    return courses.filter(type=course_type)


def query_by_teacher(courses, course_teacher):
    return courses.filter(teacherName__contains=course_teacher)


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


def default_url(request):
    pass
    return redirect("/login/")


def web_query_by_name(courses, request):
    if request.method == "GET":
        course_name = request.GET.get('course_name')
        try:
            courses = query_by_keyWord(courses, course_name)
        except:
            return render(request, 'index.html')
        return courses


def web_query_by_id(courses, request):
    if request.method == "GET":
        course_id = request.GET.get('course_id')
        try:
            courses = query_by_id(courses, course_id)
        except:
            return render(request, 'index.html')
        return courses


def web_query_by_teacher(courses, request):
    if request.method == "GET":
        teacher_name = request.GET.get('teacher_name')
        try:
            courses = query_by_teacher(courses, teacher_name)
        except:
            return render(request, 'index.html')
        return courses

# End
