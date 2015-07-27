from django import forms


class AddCourseForm(forms.Form):
    class_number = forms.IntegerField(required=True)