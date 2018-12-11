from django.shortcuts import render

from base.models import Course
from base.models import SubjectArea


def index(request):
    """
    Lists all subject areas
    """
    subjects = SubjectArea.objects.order_by('long')
    return render(request, 'bulletin/index.html', {'subjects': subjects})


def subject(request, subject_short):
    """
    Lists all courses for a given subject
    :param subject_short: the 4 letter subject abbreviation
    """
    try:
        subject = SubjectArea.objects.get_or_create(short__iexact=subject_short)
        courses = Course.objects.filter(subject_area=subject)
        return render(request, 'bulletin/subject.html', {'subject': subject, 'courses': courses})
    except SubjectArea.DoesNotExist:
        return render(request, 'bulletin/subject.html')


def course(request, subject_short, course_number):
    try:
        subject_area = SubjectArea.objects.get(short__iexact=subject_short)

        try:
            course = Course.objects.get(subject_area=subject_area, course_number=course_number)
            return render(request, 'bulletin/course.html', {'course': course})
        except Course.DoesNotExist:
            return render(request, 'bulletin/course.html', {'error': "The requested course doesn't exist."})
    except SubjectArea.DoesNotExist:
        return render(request, 'bulletin/course.html', {'error': "The requested subject doesn't exist."})
