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

    user_list = models.TextField(null=True, default='[]')
    vip_list = models.TextField(null=True, default='[]')
    super_vip_list = models.TextField(null=True, default='[]')

    def __unicode__(self):
        return self.class_number

    def add_user(self, usrname):
        this_account = Account.objects.get(username=usrname)
        if this_account.is_vip:
            vip_list = self.get_user_list('vip')
            vip_list.append(usrname)
            self.vip_list = json.dumps(vip_list)
            self.is_active = True
            self.save()
        elif this_account.is_supervip:
            supervip_list = self.get_user_list('supervip')
            supervip_list.append(usrname)
            self.super_vip_list = json.dumps(supervip_list)
            self.is_active = True
            self.save()
        else:
            user_list = self.get_user_list('user')
            user_list.append(usrname)
            self.user_list = json.dumps(user_list)
            self.is_active = True
            self.save()

    def remove_user(self, usrname):
        user_list = self.get_user_list('user')
        vip_list = self.get_user_list('vip')
        super_vip_list = self.get_user_list('supervip')

        try:
            user_list.remove(usrname)
            self.user_list = json.dumps(user_list)
        except ValueError:
            pass

        try:
            vip_list.remove(usrname)
            self.vip_list = json.dumps(vip_list)
        except ValueError:
            pass

        try:
            super_vip_list.remove(usrname)
            self.super_vip_list = json.dumps(super_vip_list)
        except ValueError:
            pass

        if self.vip_list == '[]' and self.super_vip_list == '[]' and self.user_list == '[]':
            self.is_active = False

        self.save()

    def get_first_user(self):
        user_list = self.get_user_list('user')
        vip_list = self.get_user_list('vip')
        super_vip_list = self.get_user_list('supervip')

        first_user = None

        if user_list:
            first_user = user_list[0]
        if vip_list:
            first_user = vip_list[0]
        if super_vip_list:
            first_user = super_vip_list[0]

        if first_user == None:
            return False
        return Account.objects.get(username=first_user)

    def get_user_index(self, usrname):
        user_list = self.get_user_list('user')
        vip_list = self.get_user_list('vip')
        super_vip_list = self.get_user_list('supervip')

        this_account = Account.objects.get(username=usrname)
        try:
            if this_account.is_supervip:
                user_index = super_vip_list.index(usrname)

            elif this_account.is_vip:
                user_index = len(super_vip_list) + vip_list.index(usrname)

            else:
                user_index = len(super_vip_list) + len(vip_list) + user_list.index(usrname)
        except ValueError:
            user_index = 0

        return user_index

    def get_user_list(self, type):
        jsonDec = json.decoder.JSONDecoder()

        user_list = jsonDec.decode(self.user_list)

        if type == 'user':
            user_list = jsonDec.decode(self.user_list)
        elif type == 'vip':
            user_list = jsonDec.decode(self.vip_list)
        elif type == 'supervip':
            user_list = jsonDec.decode(self.super_vip_list)

        return user_list

    def get_user(self,usrname):
        user_list = self.get_user_list('user')
        vip_list = self.get_user_list('vip')
        super_vip_list = self.get_user_list('supervip')

        user_exist = True

        try:
            user_list.index(usrname)
        except ValueError:
            try:
                vip_list.index(usrname)
            except ValueError:
                try:
                    super_vip_list.index(usrname)
                except ValueError:
                    user_exist = False

        return user_exist

class ClassLog(models.Model):
    running = models.BooleanField(default=False)
    success = models.IntegerField(default=0)
    failed = models.IntegerField(default=0)
    catchedcourse = models.TextField(default='[]')
    failedcourse = models.TextField(default='[]')

    def add_catched_course(self, class_number):
        jsonDec = json.decoder.JSONDecoder()
        class_number_list = jsonDec.decode(self.catchedcourse)
        class_number_list.append(class_number)
        self.catchedcourse = json.dumps(class_number_list)
        self.success += 1
        self.save()

    def add_failed_course(self, class_number):
        jsonDec = json.decoder.JSONDecoder()
        class_number_list = jsonDec.decode(self.failedcourse)
        class_number_list.append(class_number)
        self.failedcourse = json.dumps(class_number_list)
        self.failed += 1
        self.save()

class RunningCount(models.Model):
    count = models.IntegerField(default=0)