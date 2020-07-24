# auth:lzy
# create date:7.22
# description:历史记录相关操作


# from sqlite3.dbapi2 import Time

from django import forms
from django.shortcuts import render, redirect
from BrowseRecords import forms
from BrowseRecords import models
from BrowseRecords.models import BrowseRecords
from CoursePart import views as CP_views
from MySite import views as MS_views


# def BrowseRecords(request):
#     if request.method == 'GET':
#         try:
#             infos = Course.objects.get('Course_ID')
#         except Exception as e:
#             return HttpResponse('404')
#         else:
#             infos.g_click += 1
#             infos.save()
#             result = {
#                 'infos': infos
#
#             }
#         response = render(request, 'CourseComment/detail.html', result)
#         Course_ID = request.COOKIES.get('Course_ID', None)
#         if Course_ID:
#             Course_List_ID = Course_ID.split(',')
#             if str(infos.id) not in Course_List_ID:
#                 Course_List_ID.insert(0, str(infos.id))
#             else:
#                 Course_List_ID.remove(str(infos.id))
#                 Course_List_ID.insert(0, str(infos.id))
#             if len(Course_List_ID) > 5:
#                 Course_List_ID.pop()
#             Course_ID = ','.join(Course_List_ID)
#             print(Course_ID)
#         else:
#             Course_ID = str(infos.id)
#         response.set_cookie('Course_ID', Course_ID)
#         return response
"""
def record(request):
    global thisPageRecord
    if request.method == "GET" and \
            request.GET.get('detail_id') != '' and request.GET.get('detail_id') is not None:
        # commentForm = forms.CommentForm()
        recordForm = forms.RecordForm()
        recordID = str(request.GET.get('detail_id'))
        allRecords = get_all_records()
        thisPageRecord = query_by_id(allRecords, recordID).first()
        records = sort_by_time(thisPageRecord)
        return render(request, 'detail.html', {'record': thisPageRecord,
                                               'recordForm': recordForm,
                                               'records': records})
    elif request.method == 'POST':
        if thisPageRecord is None:
            return redirect('/index/')
        # ID = thisPageRecord.ID
        return createRecord(request)
    elif request.method == "GET" and \
            request.GET.get('page') != '' and request.GET.get('page') is not None:
        records = sort_by_time(thisPageRecord)
        recordForm = forms.RecordForm()
        return render(request, 'detail.html', {'record': thisPageRecord,
                                               'recordForm': recordForm,
                                               'records': records})
    return redirect('/index/')


def createRecord(request):
    recordForm = forms.RecordForm(request.POST)
    if recordForm.is_valid():
        # record = recordForm.cleaned_data.get('thisRecord')
        user_id = request.session.get('user_id')
        course_id = request.session.get('course_id')
        # user = user_views.query_by_id(user_id)
        record = thisPageRecord
        newRecord = models.BrowseRecords()
        newRecord.Record_ID = record
        newRecord.CourseID = course_id
        newRecord.User_ID = user_id
        newRecord.Time = Time
        newRecord.save()
        records = sort_by_time(thisPageRecord)
        newRecordForm = forms.RecordForm()
        return render(request, 'detail.html', {"record": thisPageRecord,
                                               'recordForm': newRecordForm,
                                               'records': records})
"""


def add_record(user_id, course_id):
    newRecord = models.BrowseRecords()
    newRecord.Course_ID = CP_views.query_by_id2(course_id)
    newRecord.User_ID = MS_views.query_by_id(user_id)
    newRecord.save()


def delete_all_records():
    return BrowseRecords.objects.all().delete()


"""
def sort_by_time(record):
    records = models.BrowseRecords.objects.filter(Record_ID=record)
    return records.order_by("-Time")
"""


def get_all_records():
    return models.BrowseRecords.objects.all()


def query_by_id(records, record_id):
    if record_id:
        try:
            Record = records.filter(RecordID=record_id)
        except:
            return None
        return Record.first()


def delete_by_id(record_id):
    all_records = get_all_records()
    Record = query_by_id(all_records, record_id)
    models.Course.delete(Record)


def query_by_user(user):
    return get_all_records().filter(User_ID=user).order_by("-Time")


def record(request):
    if request.method == 'POST':
        record_id = request.POST.get("delete_id")
        page_num = request.POST.get("page")
        delete_by_id(record_id)
        return redirect('/record/?page='+page_num)
    user_id = request.session.get("user_id")
    user = MS_views.query_by_id(user_id)
    my_records = query_by_user(user)
    page = 1
    if request.method == 'GET' and request.GET.get('page') is not None:
        page = request.GET.get('page')
        if my_records.count() % 10 == 0:
            total_page = int(my_records.count() / 10)
        else:
            total_page = int(my_records.count() / 10)+1
        if int(page) > total_page:
            page = total_page
            return redirect('/record/?page=' + str(page))
    return render(request, "BrowseRecords.html", {"records": my_records, "this_page": page})
