from django.db import models
from Account.models import Account

class Course(models.Model):
    class_number = models.CharField(max_length=100, unique=True)
    class_title = models.CharField(max_length=100)
    class_code = models.CharField(max_length=100)
    class_campus = models.CharField(max_length=100)
    class_time = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=False)
    users_ordered = models.ManyToManyField(Account)
    the_first = models.CharField(max_length=100)
    the_premium = models.CharField(max_length=100)

    def __unicode__(self):
        return self.class_number
