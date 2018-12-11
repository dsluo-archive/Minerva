from django.contrib import admin

from .models import Address
from .models import Building
from .models import Location
from .models import SubjectArea
from .models import Course
from .models import Campus
from .models import MeetingTime
from .models import Session

# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = ('line_one', 'line_two', 'city', 'state', 'zip_code', 'country')


admin.site.register(Address, AddressAdmin)


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')


admin.site.register(Building, BuildingAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('building', 'room')


admin.site.register(Location, LocationAdmin)


class SubjectAreaAdmin(admin.ModelAdmin):
    list_display = ('short', 'long')


admin.site.register(SubjectArea, SubjectAreaAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('_course_subject_and_number', 'name')
    search_fields = ('subject_area__short', 'course_number')

    def _course_subject_and_number(self, obj):
        value = "/".join([a.short for a in obj.subject_area.filter().order_by('short')])
        value = value + " " + obj.course_number
        return value
    _course_subject_and_number.short_description = "Course ID"


admin.site.register(Course, CourseAdmin)


#class CampusAdmin(admin.ModelAdmin):
#    inlines = [AddressInline]


admin.site.register(Campus)


class MeetingTimeAdmin(admin.ModelAdmin):
    list_display = ('_day_str', 'start', 'end')

    def _day_str(self, obj):
        value = ""
        if obj.day == 0:
            value += "SUN"
        elif obj.day == 1:
            value += "MON"
        elif obj.day == 2:
            value += "TUE"
        elif obj.day == 3:
            value += "WED"
        elif obj.day == 4:
            value += "THUR"
        elif obj.day == 5:
            value += "FRI"
        elif obj.day == 6:
            value += "SAT"
        else:
            value += ""

        return value


admin.site.register(MeetingTime, MeetingTimeAdmin)


class SessionAdmin(admin.ModelAdmin):
    raw_id_fields = ('course',)


admin.site.register(Session, SessionAdmin)

