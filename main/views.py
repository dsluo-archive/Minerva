from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, 'main/index.html')

def schedule(request: HttpRequest):
    return render(request, 'main/schedule.html')
