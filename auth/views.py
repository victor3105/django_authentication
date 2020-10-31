from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    user = request.user
    context = {'user': user}
    return render(
        request,
        'home.html',
        context
    )


def signup(request):
    return render(
        request,
        'signup.html'
    )


def login(request):
    return render(
        request
    )


def logout(request):
    return render(
        request
    )
