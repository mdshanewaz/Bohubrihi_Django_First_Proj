from django import template

register = template.Library()

def myFilter(value, arg):

    #return value + ". This a new custom text"

    return value + ". " + arg

register.filter('custome_filter', myFilter)