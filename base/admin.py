from django.contrib import admin

from .models import SubjectArea

# Register your models here.

class SubjectAreaAdmin(admin.ModelAdmin):
    list_display = ('short', 'long')

admin.site.register(SubjectArea, SubjectAreaAdmin)