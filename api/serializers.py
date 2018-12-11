from rest_framework import serializers

from base.models import Course, SubjectArea


class SubjectAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubjectArea
        fields = '__all__'


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    subject_area = SubjectAreaSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
