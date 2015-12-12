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
                    if the_course.get_user(the_user.username):
                        messages.add_message(request, messages.INFO, "toastr.warning('请不要重复添加课程','Warning!');")
                        return HttpResponseRedirect('/index/')
                    elif check[0] == '4' or (check[0] == 5 and check[1] == 0):
                        messages.add_message(request, messages.INFO, "toastr.warning('您的智商需要充值谢谢，拜托请不要选去年的课！','Warning!');")
                        return HttpResponseRedirect('/index/')
                    else:
                        the_course.add_user(the_user.username)
                        the_user.add_course(check)

                        messages.add_message(request, messages.INFO, "toastr.success('课程添加成功！', '恭喜');")
                        return HttpResponseRedirect('/index/')

                except Course.DoesNotExist:
                    messages.add_message(request, messages.INFO, "toastr.error('如若课程缺失请联系开发者', '未能找到您输入的课号所对应的课程');")
                    return HttpResponseRedirect('/index/')
            else:
                messages.add_message(request, messages.INFO, "toastr.error('请购买额外的课程包', '您的课程已用尽');")
                return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')

def DeleteCourseView(request, number):
    if request.user.is_authenticated():

        course = Course.objects.get(class_number=number)
        course.remove_user(request.user.username)

        request.user.remove_course(number)

        messages.add_message(request, messages.INFO, "toastr.success('课程已成功从您的账户中删除');")

        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')


