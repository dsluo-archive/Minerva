from django.db import models

# Create your models here.
from base.models import Session, MeetingTime
from users.models import CustomUser

__all__ = ['Schedule']


class Schedule(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE, null=True)  # null = anonymous user
    sessions = models.ManyToManyField(Session)

    def meeting_times(self):
        sessions = self.sessions.all()
        if len(sessions) == 0:
            return MeetingTime.objects.none()
        elif len(sessions) > 0:
            union = sessions[0].meeting_times.all()
            for session in sessions[1:]:
                union |= session.meeting_times.all()
            return union
