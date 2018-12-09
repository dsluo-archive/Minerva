from django.http import HttpRequest
from django.urls import reverse


def navbar_context(request: HttpRequest):
    context = {
        'pages': {
            'Home':     reverse('main:index'),
            'Schedule': 'TODO',
        }
    }

    if request.user.is_authenticated:
        context['pages']['Login'] = reverse('main:users:login')
    else:
        context['pages']['Logout'] = reverse('main:users:logout')

    return context
