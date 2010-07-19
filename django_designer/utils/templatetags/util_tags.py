from django import template
from django.utils import simplejson
from django.utils.safestring import mark_safe

register = template.Library() 

@register.filter
def json(value):
    return mark_safe(simplejson.dumps(value))
