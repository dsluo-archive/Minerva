from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

# Create your views here.

class ScheduleView(TemplateView):

    #model = Session
    template_name = 'schedule/schedule.html'
    #def get_queryset(self):
    #   return Session.objects
