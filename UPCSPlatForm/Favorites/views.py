# auth: lby
# create date: 7.20
# update date: 7.23

from django.shortcuts import render
from Favorites import models
from MySite import views as user_views
from CoursePart import views as course_views
# Create your views here.


def get_favorite_list(User):
    favorites = models.Favorites.objects.filter(User_ID=User)
    return favorites

def add_favor(user_id, course_id):
    user = user_views.query_by_id(user_id)
    course = course_views.query_by_id2(course_id)
    models.Favorites.objects.update_or_create(Course_ID = course,User_ID = user)

def delete_favor(user_id,course_id):
    pass