# auth:zbk,lby,gz
# create date:7.10
# description:

from django.contrib import admin
from django.urls import path
from django.urls import include
from MySite import views
from CoursePart import views as course_views
from CourseComment import views as comment_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('', course_views.default_url, name='default'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('captcha/', include('captcha.urls')),
    path('detail/', comment_views.detail, name='detail'),

]

