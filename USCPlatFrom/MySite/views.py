from django.shortcuts import render

# Create your views here.

#主页
def index(request):
    return render(request,'index.html')

#登陆视图
def Login(request):
    return render(request,'Login.html')

#注册视图
def register(request):
    return render(request,'register.html')

#课程管理视图
def courses(request):
    return render(request,'courses.html')

#课程详情视图
def course_detail(request):
    return render(request,'course_detail.html')