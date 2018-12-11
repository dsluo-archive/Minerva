from django.http import HttpRequest
from django.urls import reverse


def navbar_context(request: HttpRequest):
    context = {
        'pages':         {
            'Home':     reverse('main:index'),
            'Schedule': 'TODO',
            'Bulletin': reverse('bulletin:bulletin_index')
        },
        'authenticated': {
            'Settings': reverse('users:settings')
        }
    }
    return context
