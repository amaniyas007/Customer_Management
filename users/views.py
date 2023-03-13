from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from users.forms import UserForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)

                return HttpResponseRedirect("/")

        context = {
            "title": "Login",
            "error": True,
            "message": "Invalid username or password !!!"
        }
        return render(request, "users/login.html", context=context)
    else:
        context = {
            "title": "Login"
        }
        return render(request, "users/login.html", context=context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:index"))

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        pass
