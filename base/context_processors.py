from django.http import HttpRequest
from django.urls import reverse


def navbar_context(request: HttpRequest):
    context = {
        'pages':         {
            'Bulletin': reverse('bulletin:index'),
            'Schedule': reverse('schedule:schedule'),
        },
        'authenticated': {
            'Settings': reverse('users:settings')
        }
    }
    return context
