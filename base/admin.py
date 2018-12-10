from django.contrib import admin

from .models import Address
from .models import Building
from .models import SubjectArea
from .models import Course

# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = ('line_one', 'line_two', 'city', 'state', 'zip_code', 'country')


admin.site.register(Address, AddressAdmin)


class AddressInline(admin.StackedInline):
    model = Address
    extra = 1


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')
    inlines = [AddressInline]


admin.site.register(Building, BuildingAdmin)


class SubjectAreaAdmin(admin.ModelAdmin):
    list_display = ('short', 'long')


admin.site.register(SubjectArea, SubjectAreaAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('_course_subject_and_number', 'name')

    def _course_subject_and_number(self, obj):
        value = "/".join([a.short for a in obj.subject_area.filter().order_by('short')])
        value = value + " " + obj.course_number
        return value
    _course_subject_and_number.short_description = "Course ID"


admin.site.register(Course, CourseAdmin)

