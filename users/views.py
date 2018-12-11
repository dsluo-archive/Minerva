from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomUserSettingsForm


def register(request: HttpRequest):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def settings(request: HttpRequest):
    if request.method == 'POST':
        form = CustomUserSettingsForm(request.POST, instance=request.user)
        if form.has_changed() and form.is_valid():
            form.save()
    else:
        form = CustomUserSettingsForm(instance=request.user)

    return render(request, 'users/settings.html', {'form': form})
