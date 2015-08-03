import json

from django.db import models
from Account.models import Account

class Course(models.Model):
    class_number = models.CharField(max_length=100, unique=True)
    class_title = models.CharField(max_length=100)
    class_code = models.CharField(max_length=100)
    class_campus = models.CharField(max_length=100)
    class_time = models.CharField(max_length=100, null=True)

    is_active = models.BooleanField(default=False)

    users_ordered = models.TextField(null=True, default='[]')
    the_first = models.CharField(max_length=100)
    the_premium = models.CharField(max_length=100)

    def __unicode__(self):
        return self.class_number

    def add_user(self, usrname):
        this_account = Account.objects.get(username=usrname)
        if this_account.is_premium:
            self.the_premium = usrname
            self.save()
        else:
            user_list = self.get_user_list()
            user_list.append(usrname)
            self.users_ordered = json.dumps(user_list)
            self.is_active = True
            self.save()

    def remove_user(self, usrname):
        user_list = self.get_user_list()
        if self.the_first == usrname:
            self.the_first = ''
            self.save()

        elif self.the_premium == usrname:
            self.the_premium = ''
            self.save()

        try:
            user_list.remove(usrname)
        except ValueError:
            print None

        if self.the_premium == '':
            if self.the_first == '':
                if user_list == []:
                    self.is_active = False

        self.users_ordered = json.dumps(user_list)
        self.save()

    def get_first_user(self):
        user_list = self.get_user_list()
        if self.the_premium == '':
            if self.the_first == '':
                if user_list == []:
                    return None
                else:
                    first_user = user_list[0]
            else:
                first_user = self.the_first
        else:
            first_user = self.the_premium

        return Account.objects.get(username=first_user)

    def get_user_index(self, usrname):
        user_list = self.get_user_list()
        try:
            user_index = user_list.index(usrname)
        except ValueError:
            return False

        return user_index

    def get_user(self, usrname):
        user_list = self.get_user_list()
        try:
            user_list.index(usrname)
            return True
        except ValueError:
            return False

    def get_user_list(self):
        jsonDec = json.decoder.JSONDecoder()
        user_list = jsonDec.decode(self.users_ordered)
        return user_list
