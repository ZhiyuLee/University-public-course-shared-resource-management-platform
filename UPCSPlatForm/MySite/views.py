import hashlib

from django.shortcuts import render, redirect
from . import models, forms
import datetime
from django.conf import settings
import CoursePart.views as course_views


# Create your views here.

# Begin
# auth:zbk, lby
# create date:7.10
# description:

def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def index(request):
    return course_views.index(request)


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')

    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            UserID = login_form.cleaned_data.get('UserID')
            Password = login_form.cleaned_data.get('Password')

            try:
                user = models.User.objects.get(UserID=UserID, )
            except:
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if not user.has_confirmed:
                message = '该用户还未经过邮件确认！'
                return render(request, 'login/login.html', locals())

            if user.Password == hash_code(Password):
                request.session['is_login'] = True
                request.session['user_id'] = user.UserID
                request.session['user_name'] = user.UserName
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
                new_user.Password = hash_code(Password1)
                new_user.Email = Email
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(Email, code)

                message = '请前往邮箱进行确认！'
                return render(request, 'login/confirm.html', locals())
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")


def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.UserID, now)
    models.ConfirmString.objects.create(code=code, user=user, )
    return code


def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives

    subject = '来自不咕组的注册确认邮件'

    text_content = '''感谢注册，这里是不咕组的大学课程共享平台！\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>127.0.0.1:8000/confirm.com</a>，\
                    这里是不咕组的大学课程共享平台！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''

    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'login/confirm.html', locals())

    JoinDate = confirm.JoinDate
    now = datetime.datetime.now()
    if now > JoinDate + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'login/confirm.html', locals())


def query_by_id(user_id):
    if user_id:
        try:
            # all_users = models.User.objects.all()
            user = models.User.objects.get(UserID=user_id)
        except:
            return None
        return user

# End
