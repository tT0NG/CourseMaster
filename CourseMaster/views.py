# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from SyncCourseData.models import Course


def PandingView(request):
    return render(request, 'landing.html')

def FaqView(request):
    return render(request, 'faq.html')


def IndexView(request):
    if request.user.is_authenticated():
        runing_count = request.user.courses_used - request.user.courses_caught
        courses = request.user.get_courses_list()
        courses_info_list = []
        for course in courses:
            this_course = Course.objects.get(class_number=course)

            order = this_course.get_user_index(request.user.username)

            if this_course.the_first != '':
                order += 1

            if this_course.the_premium != '':
                order += 1

            running = False
            if order == 0:
                running = True

            course_dic = dict([('number', course), ('code', this_course.class_title + ' ' + this_course.class_code),
                               ('order', order+1), ('time', this_course.class_time), ('running', running)])

            courses_info_list.append(course_dic)

        if request.user.psu_is_set:
            return render(request, 'index.html', {'courses_info_list': courses_info_list, 'runing_count': runing_count})
        else:
            messages.add_message(request, messages.INFO, "toastr.success('欢迎来到Class Gotcha+','Welcome!');")
            return render(request, 'index.html',
                          {'courses_info_list': courses_info_list, 'show_welcome': True, 'runing_count': runing_count})
    else:
        return HttpResponseRedirect('/login/')
