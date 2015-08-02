# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from SyncCourseData.models import Course


def PandingView(request):
    return render(request, 'landing.html')


def IndexView(request):
    if request.user.is_authenticated():
        runing_count = request.user.courses_used - request.user.courses_caught
        courses = Course.objects.filter(users_ordered=request.user)
        courses_info_list = []
        for course in courses:

            order = [i for i, x in enumerate(course.users_ordered.all()) if x == request.user][0] + 1
            running = False
            if order == 1:
                running = True

            course_dic = dict([('number', course.class_number), ('code', course.class_title + ' ' + course.class_code),
                               ('order', order),('time', course.class_time), ('running', running)])

            courses_info_list.append(course_dic)

        if request.user.psu_is_set:
            return render(request, 'index.html', {'courses_info_list': courses_info_list, 'runing_count' : runing_count})
        else:
            messages.add_message(request, messages.INFO, "toastr.success('欢迎来到Class Gotcha+','Welcome!');")
            return render(request, 'index.html', {'courses_info_list': courses_info_list, 'show_welcome': True, 'runing_count' : runing_count})
    else:
        return HttpResponseRedirect('/login/')
