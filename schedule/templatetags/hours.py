from datetime import time

from django import template

register = template.Library()


@register.simple_tag
def hours():
    """
    Returns each hour from 8 am to 9 pm
    """
    return [time(hour=hour) for hour in range(8, 22)]
