from rest_framework import viewsets

from base.models import Course, SubjectArea
from .serializers import CourseSerializer, SubjectAreaSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all().order_by('subject_area__short', 'course_number')
    serializer_class = CourseSerializer


class SubjectAreaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubjectArea.objects.all().order_by('short')
    serializer_class = SubjectAreaSerializer
