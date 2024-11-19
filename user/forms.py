from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class MyUserRegisterForms(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('phon_number', 'email', 'first_name')

