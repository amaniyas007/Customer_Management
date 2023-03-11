from django.contrib import admin
from django.urls import path, include
from users.views import login


app_name = 'users'
urlpatterns = [
    path("login/", login, name="login"),
]
