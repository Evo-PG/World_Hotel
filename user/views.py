from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MyUserRegisterForms
from django.contrib.auth import authenticate, login, logout

def register_user(request):
    if request.method == "POST":
        form = MyUserRegisterForms(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Пользователь успешно создан")
            return redirect("index")

        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{error}")

    return redirect("index")


def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            messages.success(request, "Вы успешно вошли.")
            return redirect("index")

        messages.error(request, "Неправельный логин или пороль.")
        return redirect("index")

    return redirect("index")


def logout_user(request):
    logout(request)
    messages.success(request, "Вы успешно вышли.")
    return redirect("index")
