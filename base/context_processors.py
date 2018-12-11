from django.http import HttpRequest
from django.urls import reverse


def navbar_context(request: HttpRequest):
    context = {
        'pages':         {
            'Home':     reverse('main:index'),
            'Schedule': reverse('schedule:schedule'),
            'Bulletin': 'TODO'
        },
        'authenticated': {
            #'Settings': reverse('users:settings')
        }
    }
    return context
