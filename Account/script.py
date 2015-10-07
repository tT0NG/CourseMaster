from models import Account
from SyncCourseData.models import Course

def a():
    for user in Account.objects.all():
        user.courses_pack += user.courses_used - user.courses_caught
        user.courses_used = user.courses_caught
        user.courses_list = '[]'
        user.save()

def b():
    for user in Account.objects.all():
        if user.courses_pack > 5:
            user.is_vip = True
            user.save()
def c():
    for course in Course.objects.all():
        if 'APPT' in course.class_time:
            print course.class_number
            course.delete()

