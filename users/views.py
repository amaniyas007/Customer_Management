from django.shortcuts import render


def login(request):
    context = {
        "title": "Customer Login",
    }

    return render(request, 'users/login.html', context=context)
