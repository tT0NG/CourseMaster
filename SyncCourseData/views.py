from .models import ClassLog, RunningCount
from django.http import HttpResponseRedirect, HttpResponse

from .catchcourse import add_class, add_class2

# Create your views here.
def StartSyncView(request):
    if request.user.is_admin:
        while ClassLog.objects.get(id=1).running:
            add_class()
            print 'SyncView1 is Running'
        else:
            return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')

def StartSyncView2(request):
    if request.user.is_admin:
        while ClassLog.objects.get(id=1).running:
            add_class2()
            print 'SyncView2 is Running'
        else:
            return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')

def SwitchView(request):
    if request.user.is_admin:
        c = ClassLog.objects.get(id=1)
        c.running = not c.running
        c.save()
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')


