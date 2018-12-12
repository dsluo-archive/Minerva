from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# Create your models here.
from django.utils.translation import gettext_lazy

from .util import Weekday


class Address(models.Model):
    line_one = models.CharField(max_length=255)
    line_two = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    zip_code = models.PositiveSmallIntegerField()
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.line_one


class Building(models.Model):
    number = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    address = models.OneToOneField(Address, models.CASCADE, null=True)

    def __str__(self):
        return self.name

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
    subject_area = models.ManyToManyField(SubjectArea)
    course_number = models.CharField(max_length=255)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    lab = models.BooleanField(default=False)
    honors = models.BooleanField(default=False)
    writing = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    graduate = models.BooleanField(default=False)

    min_credit_hours = models.PositiveSmallIntegerField()
    max_credit_hours = models.PositiveSmallIntegerField(null=True)

    @property
    def suffix(self):
        suffix = ''

        if self.lab:
            suffix += 'L'
        if self.honors:
            suffix += 'H'
        if self.writing:
            suffix += 'W'
        if self.service:
            suffix += 'S'
        if self.online:
            suffix += 'E'

        return suffix

    @property
    def display_short(self):
        subject_areas = list(self.subject_area.all())
        display_subject_area = str(subject_areas[0].short) + ''.join(f'({sa.short})' for sa in subject_areas[1:])

        return f'{display_subject_area} {self.course_number}{self.suffix}'

    def __str__(self):
        return self.name


class MeetingTime(models.Model):
    # 0 is Sunday
    day = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    start = models.TimeField()
    end = models.TimeField()

    def __repr__(self):
        return f'MeetingTime({Weekday(self.day)} {self.start}-{self.end})'

    def __str__(self):
        return self.__repr__()


class Campus(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.ForeignKey(Address, models.CASCADE, null=True)

    def __str__(self):
        return self.name


def validate_lowercase(value):
    if not value.islower():
        raise ValidationError(
            gettext_lazy('%(value)s is not lowercase.'),
            params={'value': value}
        )


class Session(models.Model):
    course = models.ForeignKey(Course, models.CASCADE)
    location = models.ForeignKey(Location, models.CASCADE, null=True)
    instructor = None  # todo, nullable for instructor tbd
    campus = models.ForeignKey(Campus, models.CASCADE, null=True)

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

    def __str__(self):
        return "CRN: " + str(self.id) + " (" + self.course.name + ")"
