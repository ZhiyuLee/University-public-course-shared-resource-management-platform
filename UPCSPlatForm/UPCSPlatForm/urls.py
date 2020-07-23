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
    path('messages/', comment_views.messages, name='messages'),
    path('star/', favor_views.star, name='messages'),

]

