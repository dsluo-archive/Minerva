from django import template

register = template.Library()


@register.simple_tag
def linkify(url, text, attrs=""):
    return f'<a href="{url}" {attrs}>{text}</a>'
