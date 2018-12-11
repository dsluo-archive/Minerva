from django.urls import path

from .views import ScheduleView

app_name = 'schedule'
urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule')
]
