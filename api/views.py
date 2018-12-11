from rest_framework import viewsets

from base.models import Course, SubjectArea, Session, Address, Building, Location, MeetingTime, Campus
from .serializers import CourseSerializer, SubjectAreaSerializer, SessionSerializer, AddressSerializer, \
    BuildingSerializer, LocationSerializer, MeetingTimeSerializer, CampusSerializer


class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class BuildingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Building.objects.all().order_by('number')
    serializer_class = BuildingSerializer


class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all().order_by('building__number', 'room')
    serializer_class = LocationSerializer


class SubjectAreaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubjectArea.objects.all().order_by('short')
    serializer_class = SubjectAreaSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all().order_by('subject_area__short', 'course_number')
    serializer_class = CourseSerializer


class MeetingTimeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MeetingTime.objects.all().order_by('day', 'start')
    serializer_class = MeetingTimeSerializer


class CampusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Campus.objects.all().order_by('name')
    serializer_class = CampusSerializer


class SessionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Session.objects.all().order_by('pk')
    serializer_class = SessionSerializer
