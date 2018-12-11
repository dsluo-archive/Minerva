from django.http import HttpRequest
from django.shortcuts import render

from base.util import Weekday
from schedule.models import Schedule


def schedule(request: HttpRequest):
    if request.user.is_authenticated:
        schedule = Schedule.objects.get(user=request.user)
    else:
        schedule: Schedule = request.session.get('user', Schedule())
        schedule.save()

    sessions = list(schedule.meeting_times())

    schedule = {
        str(day): list(filter(lambda x: x.day == day, sessions)) for day in Weekday
    }

    return render(request, 'schedule/schedule.html', {'schedule': schedule})
