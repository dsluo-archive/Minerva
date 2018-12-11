from django.views.generic import TemplateView


class ScheduleView(TemplateView):
    template_name = 'schedule/schedule.html'
