# auth:gz，lzy
# create date:7.18
# description:课程评价部分操作

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from CourseComment import models, forms
from CourseComment.models import Comment
import CoursePart.views as course_view
from CoursePart.models import Course
import MySite.views as user_views


thisPageCourse: Course = None


def makeComment(request, course_id):
    commentForm = forms.CommentForm(request.POST)
    if commentForm.is_valid():
        comment = commentForm.cleaned_data.get('thisComment')  # 读取表单返回的值，返回类型为字典dict型
        user = user_views.query_by_id('123')
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
    if request.POST.get("to_someone"):  # 有此字段则为回复
        user_id = request.session['user_id']
        content = request.POST.get("content")
        strategy_id = request.POST.get("strategy")
        to_someone_id = request.POST.get("to_someone")

        # 创建新回复
        new_comment = models.Comment.objects.create(
            user_id=user_id,
            content=content,
            strategy_id=strategy_id,
            to_someone_id=to_someone_id
        )
        new_comment.save()
        result = {'status': '回复成功'}
        return JsonResponse(result)
    else:
        user_id = request.session['user_id']
        content = request.POST.get("content")
        strategy_id = request.POST.get("strategy")

        # 创建新评论
        new_comment = models.Comment.objects.create(
            author_id=user_id,
            content=content,
            strategy_id=strategy_id
        )
        new_comment.save()
        result = {'status': '评论成功'}
        return JsonResponse(result)


def detail(request):
    global thisPageCourse
    if request.method == "GET" and \
            request.GET.get('detail_id') != '' and request.GET.get('detail_id') is not None:
        commentForm = forms.CommentForm()
        courseID = str(request.GET.get('detail_id'))
        allCourses = course_view.get_all_courses()
        thisPageCourse = course_view.query_by_id(allCourses, courseID).first()
        comments = query_by_Course(thisPageCourse)
        return render(request, 'detail.html', {'course': thisPageCourse,
                                               'commentForm': commentForm,
                                               'comments':comments})
    elif request.method == 'POST':
        ID = thisPageCourse.ID
        return makeComment(request, ID)
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
    return comments.order_by("-Time")

# End