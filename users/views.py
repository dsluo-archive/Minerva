from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpRequest
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserSettingsForm


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
        settings_form = CustomUserSettingsForm(request.POST)
        password_form = PasswordChangeForm(request.user)
        if settings_form.is_valid():
            settings_form.save()
        if password_form.is_valid():
            password_form.save()
    else:
        settings_form = CustomUserSettingsForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'users/settings.html', {'settings_form': settings_form, 'password_form': password_form})
