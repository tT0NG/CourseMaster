# coding=utf-8
from django.http import HttpResponseRedirect
from django.contrib import messages

from SyncCourseData.models import Course
from Account.models import Account


# Create your views here.
def AddCourseView(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            the_user = request.user
            pack = the_user.courses_pack

            if pack > 0:
                check = request.POST['class_number']
                try:
                    the_course = Course.objects.get(class_number=check)
                    try:
                        the_course.users_ordered.get(username=the_user.username)
                        messages.add_message(request, messages.INFO, "toastr.warning('请不要重复添加课程','Warning!');")
                        return HttpResponseRedirect('/index/')
                    except Account.DoesNotExist:
                        the_course.users_ordered.add(the_user)
                        the_course.is_active = True
                        the_user.courses_pack = pack - 1
                        the_user.courses_used += 1
                        the_user.save()
                        the_course.save()
                        messages.add_message(request, messages.INFO, "toastr.success('课程添加成功！', '恭喜');")
                        return HttpResponseRedirect('/index/')

                except Course.DoesNotExist:
                    messages.add_message(request, messages.INFO, "toastr.error('如若课程缺失请联系开发者', '未能找到您输入的课号所对应的课程');")
                    return HttpResponseRedirect('/index/')
            else:
                return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')

def DeleteCourseView(request, number):
    if request.user.is_authenticated():
        course = Course.objects.get(class_number=number)
        course.users_ordered.remove(request.user)
        request.user.courses_pack += 1
        request.user.courses_used -= 1
        request.user.save()
        messages.add_message(request, messages.INFO, "toastr.success('课程已成功从您的账户中删除');")
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')

def BuyCourseView(request, howmany):
    if request.user.is_authenticated():
        # TODO:Check if user is paid
        request.user.courses_pack += int(howmany)
        request.user.save()
        return HttpResponseRedirect('/index/')
