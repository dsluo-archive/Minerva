from django.core.validators import validate_comma_separated_integer_list
from django.db import models


# Create your models here.
class Address(models.Model):
    line_one = models.CharField(max_length=255)
    line_two = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.PositiveSmallIntegerField()
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=255)


class Building(models.Model):
    number = models.PositiveSmallIntegerField(primary_key=True)
    address = models.ForeignKey(Address, models.CASCADE)


class Location(models.Model):
    building = models.ForeignKey(Building, models.CASCADE)
    room = models.PositiveSmallIntegerField()


class SubjectArea(models.Model):
    short = models.CharField(max_length=4)
    long = models.CharField(max_length=255)

    department = None  # todo


class Class(models.Model):
    crn = models.CharField(primary_key=True, validators=[validate_comma_separated_integer_list], max_length=255)
    subject_area = models.ManyToManyField(SubjectArea)

    lab = models.BooleanField(default=False)
    honors = models.BooleanField(default=False)
    writing = models.BooleanField(default=False)
    service = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    graduate = models.BooleanField(default=False)

    min_credit_hours = models.PositiveSmallIntegerField()
    max_credit_hours = models.PositiveSmallIntegerField(null=True)


class MeetingTime(models.Model):
    day = models.CharField(max_length=1)
    start = models.TimeField()
    end = models.TimeField()


class Campus(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, models.CASCADE)


class Session(models.Model):
    klass = models.ForeignKey(Class, models.CASCADE)
    location = models.ForeignKey(Location, models.CASCADE)
    instructor = None  # todo, nullable for instructor tbd
    campus = None  # todo

    # spr = spring
    # fal = fall

    # summer sessions:
    # thr = thru session
    # ext = extended
    # may = maymester
    # s1 = short session 1
    # s2 = short session 2
    session = models.CharField(max_length=3, validators=[str.islower])

    max_seats = models.PositiveSmallIntegerField()
    filled_seats = models.PositiveSmallIntegerField()

    meeting_times = models.ManyToManyField(MeetingTime)
