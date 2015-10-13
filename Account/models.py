import json
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):

        """
        Creates and saves a User with the given email, username and password.
        """

        if not email:
            raise ValueError('Users must have a vaild email address')

        if not kwargs.get('username'):
            raise ValueError('Users must have a vaild username')

        if not kwargs.get('campus'):
            raise ValueError('Users must choose a vaild campus')

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username'), campus=kwargs.get('campus')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    campus = models.CharField(max_length=40, blank=True)

    psu_account = models.CharField(max_length=40)
    psu_password = models.CharField(max_length=100)
    psu_is_set = models.BooleanField(default=False)

    courses_pack = models.IntegerField(default=0)
    courses_caught = models.IntegerField(default=0)
    courses_used = models.IntegerField(default=0)
    courses_failed = models.IntegerField(default=0)
    courses_list = models.TextField(default='[]')
    courses_caught_list = models.TextField(default='[]')
    courses_failed_list = models.TextField(default='[]')


    is_admin = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)
    is_supervip = models.BooleanField(default=False)
    is_correct = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'campus']

    def __unicode__(self):
        return self.email

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_courses_list(self, kind):
        jsonDec = json.decoder.JSONDecoder()

        if kind == 'running':
            courses_list = jsonDec.decode(self.courses_list)
        elif kind == 'caught':
            courses_list = jsonDec.decode(self.courses_caught_list)
        elif kind == 'failed':
            courses_list = jsonDec.decode(self.courses_failed_list)
        else:
            courses_list = []
        return courses_list

    def add_course(self, class_number):
        courses_list = self.get_courses_list('running')
        courses_list.append(class_number)
        self.courses_list = json.dumps(courses_list)

        self.courses_pack -= 1
        self.courses_used += 1
        self.save()

    def add_course_caught(self, class_number):
        caught_list = self.get_courses_list('caught')
        caught_list.append(class_number)
        self.courses_caught_list = json.dumps(caught_list)
        courses_list = self.get_courses_list('running')
        courses_list.remove(class_number)
        self.courses_list = json.dumps(courses_list)
        self.save()

    def add_course_failed(self, class_number):
        courses_list = self.get_courses_list('failed')
        courses_list.append(class_number)
        self.courses_failed += 1
        self.courses_failed_list = json.dumps(courses_list)
        self.save()

    def remove_course(self, class_number):
        courses_list = self.get_courses_list('running')
        courses_list.remove(class_number)
        
        self.courses_list = json.dumps(courses_list)

        self.courses_pack += 1
        self.courses_used -= 1
        self.save()



    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin
