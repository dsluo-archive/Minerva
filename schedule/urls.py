from django.urls import path
from schedule.views import ScheduleView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


app_name = 'schedule'
urlpatterns = [
    path('/', ScheduleView.as_view(), name='schedule')
]
