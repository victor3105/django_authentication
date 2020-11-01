from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse


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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = UserCreationForm()
    context = {'form': form}
    # user = User.objects.create_user(username=username, password=password)
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     redirect('home')
    return render(
        request,
        'signup.html',
        context
    )


class Login(LoginView):
    template_name = 'login.html'


class Logout(LogoutView):
    template_name = 'logout.html'
