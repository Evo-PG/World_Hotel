from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class MyUserRegisterForms(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('phon_number', 'email', 'first_name')
        widgets = {
            'phon_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш номер телефона'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Подтвердите пароль'
            }),
        }
