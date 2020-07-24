# auth:gz，lzy
# create date:7.18
# description:课程评价部分操作

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from BrowseRecords.views import add_record
from CourseComment import models, forms
from CourseComment.models import Comment
import CoursePart.views as course_view
from CoursePart.models import Course
import MySite.views as user_views

thisPageCourse: Course = None


def makeComment(request):
    commentForm = forms.CommentForm(request.POST)
    if commentForm.is_valid():
        comment = commentForm.cleaned_data.get('thisComment')  # 读取表单返回的值，返回类型为字典dict型
        user_id = request.session.get('user_id')
        user = user_views.query_by_id(user_id)
        course = thisPageCourse
        newComment = models.Comment()
        newComment.Comment_text = comment
        newComment.Course_ID = course
        newComment.Comment_User_ID = user
        newComment.save()
        comments = query_by_Course(thisPageCourse)
        newCommentForm = forms.CommentForm()
        return render(request, 'detail.html', {"course": thisPageCourse,
                                               'commentForm': newCommentForm,
                                               'comments': comments})


def replyComment(request):
    commentForm = forms.CommentForm(request.POST)
    if commentForm.is_valid():
        comment = commentForm.cleaned_data.get('thisComment')
        user_id = request.session.get('user_id')
        user = user_views.query_by_id(user_id)
        course = thisPageCourse
        to_comment_id = commentForm.cleaned_data.get("ToCommentID")
        to_comment = query_by_id(to_comment_id)

        # 创建新回复
        newComment = models.Comment()
        newComment.To_Comment_ID = to_comment
        newComment.Comment_text = comment
        newComment.Course_ID = course
        newComment.Comment_User_ID = user
        newComment.save()
        comments = query_by_Course(thisPageCourse)
        newCommentForm = forms.CommentForm()
        return render(request, 'detail.html', {"course": thisPageCourse,
                                               'commentForm': newCommentForm,
                                               'comments': comments})


def detail(request):
    global thisPageCourse
    if request.method == "GET" and \
            request.GET.get('detail_id') != '' and request.GET.get('detail_id') is not None:
        commentForm = forms.CommentForm()
        courseID = str(request.GET.get('detail_id'))
        allCourses = course_view.get_all_courses()
        thisPageCourse = course_view.query_by_id(allCourses, courseID).first()
        comments = query_by_Course(thisPageCourse)
        user_id = request.session.get('user_id')
        add_record(user_id, thisPageCourse.ID)
        return render(request, 'detail.html', {'course': thisPageCourse,
                                               'commentForm': commentForm,
                                               'comments': comments})
    elif request.method == 'POST' and \
            request.POST.get("ToCommentID") == '*':
        if thisPageCourse is None:
            return redirect('/index/')
        # ID = thisPageCourse.ID
        return makeComment(request)
    elif request.method == 'POST' and \
            request.POST.get("ToCommentID") != '*':
        if thisPageCourse is None:
            return redirect('/index/')
        # ID = thisPageCourse.ID
        return replyComment(request)
    elif request.method == "GET" and \
            request.GET.get('page') != '' and request.GET.get('page') is not None:
        comments = query_by_Course(thisPageCourse)
        commentForm = forms.CommentForm()
        return render(request, 'detail.html', {'course': thisPageCourse,
                                               'commentForm': commentForm,
                                               'comments': comments})
    return redirect('/index/')


# def index(request):
#     return render(request, comment.html)
#
#
# def add_comments(comment_text, request):
#     new_comment = models.Evaluation()
#     new_comment.text = comment_text
#     new_comment.save()
#
#
# def delete_comments(comment, request):
#     comment.is_deleted = True
#     comment.save()
#

# def edit_comments(comment_text, request):
#     comment = models.Evaluation()
#     comment.text = comment.description
#     comment.save()


def query_by_Course(course):
    comments = models.Comment.objects.filter(Course_ID=course)
    '''
    for comment in comments:
        if comment.To_Comment_ID is not None:
            to_id = comment.To_Comment_ID
            for to_comment in comments:
                if to_comment.id == to_id:
                    temp = comment
                    comments.delete(comment)
                    break
    '''
    return comments.order_by("-Time")


def query_by_id(ID):
    comment = models.Comment.objects.get(Comment_ID=ID)
    return comment


def query_by_user(user):
    comments = models.Comment.objects.filter(Comment_User_ID=user)
    return comments.order_by("-Time")


def get_user_messages(user):
    messages = models.Comment.objects.filter(To_Comment_ID__Comment_User_ID=user)
    return messages.order_by("-Time")


def my_comments(request):
    user_id = request.session.get('user_id')
    user = user_views.query_by_id(user_id)
    myComments = query_by_user(user)
    return render(request, "my_comments.html", {"my_comments": myComments})


def messages(request):
    user_id = request.session.get('user_id')
    user = user_views.query_by_id(user_id)
    Messages = get_user_messages(user)
    return render(request, "messages.html", {"messages": Messages})

# End
