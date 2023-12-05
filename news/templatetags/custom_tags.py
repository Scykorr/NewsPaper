import datetime

from django import template

register = template.Library()


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.datetime.now(datetime.UTC).strftime(format_string)
