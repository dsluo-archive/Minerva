from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from base.models import Session

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class ScheduleView(TemplateView):

    #model = Session
    template_name = 'main/schedule.html'
    #def get_queryset(self):
    #   return Session.objects