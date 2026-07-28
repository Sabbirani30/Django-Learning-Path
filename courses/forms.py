from django import forms
class StudentRegistration (forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    age = forms.IntegerField()
    course = forms.CharField()
    batch = forms.IntegerField()
    department = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
