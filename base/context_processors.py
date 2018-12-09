from django.urls import reverse


def navbar_context(_):
    return {
        'pages': {
            'Home':     reverse('main:index'),
            'Schedule': 'TODO'
        }
    }
