# auth: lby,gz
# create date: 7.20
# update date: 7.23

from django.shortcuts import render
from Favorites import models
from MySite import views as user_views
from CoursePart import views as course_views
import MySite.views as user_views
import CoursePart.views as course_views


def get_favorite_list(User):
    favorites = models.Favorites.objects.filter(User_ID=User)
    return favorites


def add_favor(user_id, course_id):
    user = user_views.query_by_id(user_id)
    course = course_views.query_by_id2(course_id)
    models.Favorites.objects.update_or_create(Course_ID=course, User_ID=user)


def delete_favor(user_id, course_id):
    user = user_views.query_by_id(user_id)
    course = course_views.query_by_id2(course_id)
    favor = models.Favorites.objects.get(Course_ID=course, User_ID=user)
    models.Favorites.delete(favor)


def star(request):
    user = user_views.query_by_id(request.session.get('user_id'))
    stars = get_favorite_list(user)
    real_stars = []
    for star in stars:
        for course in course_views.get_all_courses():
            if course == star.Course_ID:
                real_stars.append(course)
                break
    return render(request, 'star.html', {'courses': real_stars})
