from django.urls import path

from .views import course
from .views import index
from .views import subject

app_name = 'bulletin'
urlpatterns = [
    path('', index, name='index'),
    path('<str:subject_short>/', subject, name="subject"),
    path('<str:subject_short>/<int:course_number>/', course, name='course')
]
