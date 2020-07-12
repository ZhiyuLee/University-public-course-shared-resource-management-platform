# auth:zbk，lby
# create date:7.10
# description:



from django.shortcuts import render,redirect
from.import models,forms
import datetime
from django.conf import settings
import CoursePart.views as course_views


<<<<<<< HEAD
=======


# Create your views here.

# Begin
# auth:zbk
# create date:7.10
# description:


>>>>>>> 8dabe4a308aac773cf951a9e225a19278278c71c
def index(request):
    return course_views.index(request)


def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            UserID = login_form.cleaned_data.get('UserID')
            Password = login_form.cleaned_data.get('Password')
            try:
                user = models.User.objects.get(UserID=UserID)
            except:
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())
            if user.Password == Password:
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            UserID = register_form.cleaned_data.get('UserID')
            UserName = register_form.cleaned_data.get('UserName')
            Password1 = register_form.cleaned_data.get('Password1')
            Password2 = register_form.cleaned_data.get('Password2')
            Email = register_form.cleaned_data.get('Email')

            if Password1 != Password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_id_user = models.User.objects.filter(UserID=UserID)
                if same_id_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(Email=Email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.UserID = UserID
                new_user.UserName = UserName
                new_user.Password = Password1
                new_user.Email = Email
                new_user.save()

                return redirect('/login/')

        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    pass
    return redirect("/login/")


