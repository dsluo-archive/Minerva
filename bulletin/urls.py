from django.urls import path, include

from .views import index
from .views import subject
from .views import course

app_name = 'bulletin'
urlpatterns = [
    path('', index, name='bulletin_index'),
    path('<str:subject>/', subject, name="bulletin_subject"),
    path('<str:subject>/<int:course>/', course, name='bulletin_course')
]
