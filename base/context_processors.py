from django.http import HttpRequest
from django.urls import reverse


def navbar_context(request: HttpRequest):
    context = {
        'pages':         {
            'Home':     reverse('main:index'),
            'Schedule': 'TODO',
            'Bulletin': reverse('bulletin:index')
        },
        'authenticated': {
            'Settings': reverse('users:settings')
        }
    }
    return context
