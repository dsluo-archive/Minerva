from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'bulletin/index.html')

def subject(request, subject):
    return render(request, 'bulletin/subject.html')

def course(request, subject, course):
    return render(request, 'bulletin/course.html')