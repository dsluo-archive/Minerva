from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest
from django.shortcuts import render, redirect


def login(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('main:index')
        else:
            # Return an 'invalid login' error message.
            ...
    else:
        login_form = AuthenticationForm(request)
        return render(request, 'login.html', {'login_form': login_form})

def register(request: HttpRequest):
    return render(request, 'register.html')
