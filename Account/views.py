# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.core.context_processors import csrf

from forms import MyRegistrationForm

def LoginView(request):
    '''
    Login View
    '''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect('/index/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def LogoutView(request):
    '''
    Log the user out
    '''
    auth_logout(request)
    return HttpResponseRedirect('/login')


def RegisterView(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = MyRegistrationForm()
        print 'the form submit error'

    #args = {}
    #args.update(csrf(request))
    #args['form'] = MyRegistrationForm()
    return render(request, 'register.html', {'form': form})
