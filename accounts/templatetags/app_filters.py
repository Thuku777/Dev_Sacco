from django import template

register = template.Library()

@register.filter
def is_false(arg): 
    return arg is False
    
# @register.filter(name='is_false')
# def is_false(value, arg):
#     return value.replace(arg, '')

#Reminder create total count custom filter tag