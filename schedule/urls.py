from django.urls import path

from .views import schedule

app_name = 'schedule'
urlpatterns = [
    path('', schedule, name='schedule')
]
