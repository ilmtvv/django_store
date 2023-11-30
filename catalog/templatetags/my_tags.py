from django import template

register = template.Library()

@register.simple_tag
def image_tag(url):
    return url

@register.filter(needs_autoescape=True)
def image_filter(url, autoescape=True):
    return url