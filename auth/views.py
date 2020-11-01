from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from .forms import SignupForm, LoginForm


def home(request):
    user = request.user
    context = {'user': user}
    return render(
        request,
        'home.html',
        context
    )


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = SignupForm()
    context = {'form': form}
    return render(
        request,
        'signup.html',
        context
    )


class Login(LoginView):
    template_name = 'login.html'
    form_class = LoginForm


class Logout(LogoutView):
    template_name = 'logout.html'
