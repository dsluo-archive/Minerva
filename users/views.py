from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


def register(request: HttpRequest):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
