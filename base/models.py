from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy


class Building(models.Model):
    number = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class Address(models.Model):
    line_one = models.CharField(max_length=255)
    line_two = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    zip_code = models.PositiveSmallIntegerField()
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=255)
    building = models.OneToOneField(Building, models.CASCADE, null=True)

    def __str__(self):
        return self.line_one


class Location(models.Model):
    building = models.ForeignKey(Building, models.CASCADE)
    room = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.building.name + " " + str(self.room)


class SubjectArea(models.Model):
    short = models.CharField(max_length=4, unique=True)
    long = models.CharField(max_length=255)

    department = None  # todo

    def __str__(self):
        return self.long


class Course(models.Model):
    subject_area = models.ManyToManyField(SubjectArea, through='SubjectAreaCourse')
    course_number = models.CharField(max_length=255)

    name = models.CharField(max_length=255)

    lab = models.BooleanField(default=False)
    honors = models.BooleanField(default=False)
    writing = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    graduate = models.BooleanField(default=False)

    min_credit_hours = models.PositiveSmallIntegerField()
    max_credit_hours = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name


class SubjectAreaCourse(models.Model):
    subject_area = models.ForeignKey(SubjectArea, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('subject_area', 'course')


class MeetingTime(models.Model):
    day = models.CharField(max_length=1)
    start = models.TimeField()
    end = models.TimeField()


class Campus(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.ForeignKey(Location, models.CASCADE)


def validate_lowercase(value):
    if not value.islower():
        raise ValidationError(
            gettext_lazy('%(value)s is not lowercase.'),
            params={'value': value}
        )


class Session(models.Model):
    course = models.ForeignKey(Course, models.CASCADE)
    location = models.ForeignKey(Location, models.CASCADE)
    instructor = None  # todo, nullable for instructor tbd
    campus = models.ForeignKey(Campus, models.CASCADE)

    # spr = spring
    # fal = fall

    # summer sessions:
    # thr = thru session
    # ext = extended
    # may = maymester
    # s1 = short session 1
    # s2 = short session 2
    semester = models.CharField(max_length=3, validators=[validate_lowercase])

    max_seats = models.PositiveSmallIntegerField()
    filled_seats = models.PositiveSmallIntegerField()

    meeting_times = models.ManyToManyField(MeetingTime)