from django.shortcuts import render

from base.models import Course
from base.models import SubjectArea


def index(request):
    """
    Lists all subject areas
    """
    subjects = SubjectArea.objects.order_by('short')
    return render(request, 'bulletin/index.html', {'subjects': subjects})


def subject(request, subject_short):
    """
    Lists all courses for a given subject
    :param subject_short: the 4 letter subject abbreviation
    """
    try:
        subject = SubjectArea.objects.get(short__iexact=subject_short)
        courses = Course.objects.filter(subject_area=subject).order_by('course_number')
        return render(request, 'bulletin/subject.html', {'subject': subject, 'courses': courses})
    except SubjectArea.DoesNotExist:
        return render(request, 'bulletin/subject.html')


def course(request, subject_short, course_number):
    try:
        courses = Course.objects.filter(subject_area__short__iexact=subject_short, course_number=course_number)
        return render(request, 'bulletin/course.html', {'courses': courses})
    except Course.DoesNotExist:
        return render(request, 'bulletin/course.html', {'error': "The requested course doesn't exist."})
