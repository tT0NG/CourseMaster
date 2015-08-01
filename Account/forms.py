#coding=utf-8
from django import forms
from .models import Account  # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    SCHOOLS = (
        ('', '选择校区'),
        ('UP', 'University Park'),
        ('None', 'Unavailable'),
        ('None', 'Unavailable'),
        ('None', 'Unavailable'),
    )
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    campus = forms.ChoiceField(required=True,
                               choices=SCHOOLS)

    class Meta:
        model = Account
        fields = ('username', 'email', 'campus', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.campus = self.cleaned_data['campus']

        if commit:
            user.save()

        return user
