from django import template

register = template.Library()
@register.filter(name="getval")
def getval(dict,key):
    print("replies:",dict.get(key))
    return dict.get(key)