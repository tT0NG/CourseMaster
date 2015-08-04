from .models import ClassLog
from django.http import HttpResponseRedirect, HttpResponse

import time

from .catchcourse import add_class

# Create your views here.
def StartSyncView(request):
    if request.user.is_admin:
        c = ClassLog.objects.get(id=1)
        if c.running:
            while True:
                add_class()
                c.count += 1
                c.save()
                time.sleep(10)
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


