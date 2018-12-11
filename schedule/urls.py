from schedule.views import ScheduleView
from django.urls import path
from django.urls import path

from schedule.views import ScheduleView

app_name = 'schedule'
urlpatterns = [
    path('', ScheduleView.as_view(), name='schedule')
]
