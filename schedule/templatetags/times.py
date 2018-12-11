from datetime import time

from django import template

from base.util import Weekday

register = template.Library()


@register.simple_tag
def hours():
    """
    Returns each hour from 8 am to 9 pm
    """
    return [time(hour=hour) for hour in range(8, 22)]


@register.simple_tag
def days():
    return list(str(day) for day in Weekday)
