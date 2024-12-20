from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import MyUser

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ("phon_number", "first_name", "email")

    def clean_password2(self):
        password1 = self.cleaned_data.git("password1")
        password2 = self.cleaned_data.git("password2")
        if  password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField

    class Meta:
        model = MyUser
        fields = ("password", "is_admin")


class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('phon_number', 'first_name', 'statys', 'is_admin')
    list_filter = ('is_admin', 'statys','create_date')
    fieldsets = (
        (None, {"fields": (
            "password",
            "first_name",
            "last_name",
            "email",
            "statys",)}),
        ("Permission", {"fields": ("is_admin",)})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name",
                "phon_number",
                "email",
                "password1",
                "password2"),
        }),
    )
    search_fields = ("phon_number", "first_name", "email")
    ordering = ("phon_number",)
    filter_horizontal = ()


admin.site.register(MyUser, UserAdmin)
