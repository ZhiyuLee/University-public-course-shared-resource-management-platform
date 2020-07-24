# auth:gz , lby
# create date:7.10
# update date:7.23
# description:课程部分操作

from django.shortcuts import render
from CoursePart import models, tests
import decimal
from django.shortcuts import render, redirect
from Favorites.views import delete_favor,add_favor,get_favorite_list
import MySite.views as user_view
from MySite import forms
import hashlib


def index(request):
    # tests.testCoursePart.test_add_course(self=None)
    courses = get_all_courses()
    if request.GET.get('course_name') != "" and \
            request.GET.get('course_name') is not None:
        courses = web_query_by_name(courses, request)
    if request.GET.get('course_college') != "" and \
            request.GET.get('course_college') is not None:
        courses = web_query_by_college(courses, request)
    if request.GET.get('course_teacher') != "" and \
            request.GET.get('course_teacher') is not None:
        courses = web_query_by_teacher(courses, request)
    if request.GET.get('course_type') != "" and \
            request.GET.get('course_type') is not None:
        courses = web_query_by_type(courses, request)
    if request.method == 'POST':
        # decision = request.POST.get('decision_id')
        if request.POST.get('decision_id') == "like":
            add_favor(request.session.get('user_id'), request.POST.get('star_id'))
        else:
            delete_favor(request.session.get('user_id'), request.POST.get('star_id'))
        return redirect('/index/')
    # all_course = get_all_courses()
    user = user_view.query_by_id(request.session.get('user_id'))
    stars = get_favorite_list(user)
    real_stars = []
    for star in stars:
        for course in get_all_courses():
            if course == star.Course_ID:
                real_stars.append(course)
                break
    return render(request, 'index.html', {'courses': courses, 'stars': real_stars})


def get_all_courses():
    return models.Course.objects.all()


# 返回query set 要用first()取第一个才是结果
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
    all_courses = get_all_courses()
    course = query_by_id(all_courses, course_id)
    models.Course.delete(course)


# 课程类别, 授课教师, 授课学院, 课程学分, 学时安排
def add_course(course_name,
               course_type, course_teacher,
               course_collage, course_credit,
               course_time):
    new_course = models.Course()
    new_course.college = course_collage
    new_course.credit = course_credit
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


def query_by_id2(course_id):
    courses = models.Course.objects.all()
    if course_id:
        try:
            course = courses.filter(ID=course_id)
        except:
            return None
        return course.first()


def web_query_by_teacher(courses, request):
    if request.method == "GET":
        teacher_name = request.GET.get('course_teacher')
        try:
            courses = query_by_teacher(courses, teacher_name)
        except:
            return render(request, 'index.html')
        return courses


def web_query_by_type(courses, request):
    if request.method == "GET":
        course_type = request.GET.get('course_type')
        try:
            courses = query_by_type(courses, course_type)
        except:
            return render(request, 'index.html')
        return courses


def query_by_collage(courses, college):
    return courses.filter(college__contains=college)


def web_query_by_college(courses, request):
    if request.method == "GET":
        college = request.GET.get('course_college')
        try:
            courses = query_by_collage(courses, college)
        except:
            return render(request, 'index.html')
        return courses


def my_information(request):
    from MySite import models
    User = models.User.objects.get(UserID=request.session['user_id'])
    return render(request, "my_information.html", {"User": User})


def about_us(request):
    return render(request, "about_us.html")


def editusername(request):
    from MySite import models
    if request.method == "POST":
        user_editform = forms.EditUserNameForm(request.POST)
        if user_editform.is_valid():
            UserName = user_editform.cleaned_data.get('UserName')

            User = models.User.objects.get(UserID=request.session['user_id'])
            User.UserName = UserName
            User.save()

            return render(request, 'my_information.html', locals())
        else:
            return render(request, 'editusername.html', locals())
    user_editform = forms.EditUserNameForm()
    return render(request, 'editusername.html', locals())


def editpassword(request):
    from MySite import models
    if request.method == "POST":
        user_editform = forms.EditPasswordForm(request.POST)
        if user_editform.is_valid():
            Password = user_editform.cleaned_data.get('Password')

            User = models.User.objects.get(UserID=request.session['user_id'])
            User.Password = hash_code(Password)
            User.save()

            return render(request, 'my_information.html', locals())
        else:
            return render(request, 'editpassword.html', locals())
    user_editform = forms.EditPasswordForm()
    return render(request, 'editpassword.html', locals())


def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

# End
