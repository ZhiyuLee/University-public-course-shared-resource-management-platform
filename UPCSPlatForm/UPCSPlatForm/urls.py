# auth:zbk,lby,gz
# create date:7.10
# description:

from django.contrib import admin
from django.urls import path
from django.urls import include
from MySite import views
from CoursePart import views as course_views
from CourseComment import views as comment_views
from spider import views as spider_views
from Favorites import views as favor_views
from MySite.views import ForgetPwdView,ModifyView
from BrowseRecords import views as BR_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('', course_views.default_url, name='default'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('captcha/', include('captcha.urls')),
    path('confirm/', views.user_confirm),
    path('detail/', comment_views.detail, name='detail'),
    path('spider/', spider_views.index, name='spider'),
    path('my_comments/', comment_views.my_comments, name='my_comment'),
    path('my_information/', course_views.my_information, name='my_information'),
    path('messages/', comment_views.messages, name='messages'),
    path('star/', favor_views.star, name='messages'),
    path('forget/', ForgetPwdView.as_view(), name='forget'),
    path('reset/', views.reset, name='reset'),
    path('modify/', ModifyView.as_view(), name='modify'),
    path('editusername/', course_views.editusername, name='editusername'),
    path('editpassword/', course_views.editpassword, name='editpassword'),
    path('record/', BR_views.record, name='record'),
    path('about_us/', course_views.about_us, name="about_us"),


]

