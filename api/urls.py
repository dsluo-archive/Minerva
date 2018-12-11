from django.urls import path, include
from rest_framework import routers

from .views import CourseViewSet, SubjectAreaViewSet

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)
router.register(r'subject_area', SubjectAreaViewSet)

# app_name = 'api'
urlpatterns = [
    path('', include(router.urls))
]
