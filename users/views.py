from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomUserSettingsForm


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


@login_required
def settings(request: HttpRequest):
    if request.method == 'POST':
        form = CustomUserSettingsForm(request.POST)
        if form.has_changed() and form.is_valid():
            form.save()
    else:
        form = CustomUserSettingsForm(instance=request.user)

    return render(request, 'users/settings.html', {'form': form})
