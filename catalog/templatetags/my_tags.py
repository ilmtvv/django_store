from django import template

from config import settings

register = template.Library()

@register.simple_tag
def image_tag(url):
    return f'{settings.MEDIA_URL}{url}'

@register.filter(needs_autoescape=True)
def image_filter(url, autoescape=True):
    return f'{settings.MEDIA_URL}{url}'