from django import template

register = template.Library()

@register.filter
def addSpace(value):
    if value is not None:
        return value.replace(","," , ")

@register.filter
def getList(value):
    return range(value)