from .models import ClassLog, RunningCount
from django.http import HttpResponseRedirect, HttpResponse

import time

from .catchcourse import add_class, add_class2

# Create your views here.
def StartSyncView(request):
    if request.user.is_admin:
        while ClassLog.objects.get(id=1).running:
            print 'here'
            c = RunningCount.objects.get(id=1)
            add_class()
            c.count += 1
            c.save()
            time.sleep(0.1)
        else:
            return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')

def StartSyncView2(request):
    if request.user.is_admin:
        while ClassLog.objects.get(id=1).running:
            print 'here22'
            c = RunningCount.objects.get(id=1)
            add_class2()
            c.count += 1
            c.save()
            time.sleep(0.1)
        else:
            return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')

def SwitchView(request):
    if request.user.is_admin:
        c = ClassLog.objects.get(id=1)
        c.running = not c.running
        c.save()
        return HttpResponse(c.running)
    else:
        return HttpResponseRedirect('/login/')


