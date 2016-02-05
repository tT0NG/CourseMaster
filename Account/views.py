# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.core.context_processors import csrf
from Account.models import Account

from SyncCourseData.models import Course

from forms import MyRegistrationForm

def LoginView(request):
    '''
    Login View
    '''
    if not request.user.is_authenticated():
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = authenticate(email=request.POST['username'], password=request.POST['password'])
                if user is not None:
                    auth_login(request, user)
                    if user.psu_is_set:
                        messages.add_message(request, messages.INFO, "toastr.success('欢迎回到Class Gotcha+','Welcome back!');")
                    return HttpResponseRedirect('/index/')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/index/')


def LogoutView(request):
    '''
    Log the user out
    '''
    auth_logout(request)
    return HttpResponseRedirect('/')


def RegisterView(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = MyRegistrationForm()

    return render(request, 'register.html', {'form': form})


def AddPsuInfoView(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            try:
                request.user.psu_account = request.POST['psuAccount']
            except:
                pass
            request.user.psu_password = request.POST['psuPass']
            request.user.psu_is_set = True
            if not request.user.is_correct:
                request.user.is_correct = True
                request.user.courses_failed = 0
            request.user.save()
            return HttpResponseRedirect('/index/')

    else:
        return HttpResponseRedirect('/login/')

def InitDataView(request):
    if request.user.is_authenticated():
        users = Account.objects.all()
        for user in users:
            user.remove_course_all()

        courses = Course.objects.all()
        for course in courses:
            course.is_active = False
            course.user_list = []
            course.vip_list = []
            course.super_vip_list = []
            course.save()

        return HttpResponseRedirect('/steve/')
    else:
        return HttpResponseRedirect('/login/')