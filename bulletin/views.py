from django.shortcuts import render
from django.template import loader

from base.models import SubjectArea

# Create your views here.

# Displays the index of the bulletin view. Includes a list of subject areas.
def index(request):
    # Obtain a list of subject areas from the database.
    list_of_subjects = SubjectArea.objects.order_by('long')

    # Create a dictionary containing the list.
    context = {
        'list_of_subjects': list_of_subjects,
    }

    # Pass the dictionary into the template for the index page.
    return render(request, 'bulletin/index.html', context)

def subject(request, subject):
    return render(request, 'bulletin/subject.html')

def course(request, subject, course):
    return render(request, 'bulletin/course.html')