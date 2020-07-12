# auth:zbk,lby,gz
# create date:7.10
# description:

from django.contrib import admin
from django.urls import path
from django.urls import include
from MySite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('captcha/', include('captcha.urls')),
<<<<<<< HEAD
=======

]
>>>>>>> 8dabe4a308aac773cf951a9e225a19278278c71c

]
