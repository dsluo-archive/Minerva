from django.urls import path
from base.views import ScheduleView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import index

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('schedule/', ScheduleView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
