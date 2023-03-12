from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    context = {
        "title": "Home",
    }
    return render(request, "web/index.html", context=context)
