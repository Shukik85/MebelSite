from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout
from register.forms import UserRegisterForm, UserLoginForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно!")
            user = form.save()
            login(request, user)
            return redirect("news:News")
        else:
            messages.error(request, "Ошибка регистрации.")
    else:
        form = UserRegisterForm()
    return render(request, "reg/register.html", {"form": form, "title": "Регистрация"})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("news:News")
    else:
        form = UserLoginForm()
    return render(request, "reg/login.html", {"form": form, "title": "Вход"})


def user_logout(request):
    logout(request)
    return redirect("register:Login")
