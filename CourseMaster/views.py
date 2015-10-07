# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from SyncCourseData.models import Course
from SyncCourseData.models import ClassLog


def PandingView(request):
    return render(request, 'landing.html')

def FaqView(request):
    return render(request, 'faq.html')


def IndexView(request):
    if request.user.is_authenticated():
        course_caught_total = ClassLog.objects.get(id=1).success
        actvating = Course.objects.filter(is_active=True).count()
        waiting = 0
        running_count = request.user.courses_used - request.user.courses_caught
        courses = request.user.get_courses_list('running')
        courses_info_list = []
        for course in courses:
            this_course = Course.objects.get(class_number=course)
            order = this_course.get_user_index(request.user.username)
            running = True
            if order != 0:
                running = False
                waiting += 1
            course_dic = dict([('number', course), ('code', this_course.class_title + ' ' + this_course.class_code),
                               ('order', order + 1), ('time', this_course.class_time), ('running', running)])
            courses_info_list.append(course_dic)

        courses = request.user.get_courses_list('caught')
        courses_caught_list = []
        for course in courses:
            this_course = Course.objects.get(class_number=course)
            course_dic = dict([('number', course), ('code', this_course.class_title + ' ' + this_course.class_code),
                            ('time', this_course.class_time)])
            courses_caught_list.append(course_dic)
        courses_caught_num = len(courses_caught_list)

        if request.user.psu_is_set:
            return render(request, 'index.html',
                          {'courses_info_list': courses_info_list, 'courses_caught_list': courses_caught_list, 'runing_count': running_count,
                           'waiting': waiting, 'course_caught': course_caught_total, 'actvating': actvating, 'courses_caught_num': courses_caught_num})
        else:
            messages.add_message(request, messages.INFO, "toastr.success('欢迎来到Class Gotcha+','Welcome!');")
            return render(request, 'index.html',
                          {'courses_info_list': courses_info_list, 'courses_caught_list': courses_caught_list, 'show_welcome': True, 'runing_count': running_count,
                           'waiting': waiting, 'course_caught': course_caught_total, 'actvating': actvating, 'courses_caught_num': courses_caught_num})

    else:
        return HttpResponseRedirect('/login/')
