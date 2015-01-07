from django.template import Library

register = Library()


@register.filter
def get(dict, key, default=''):
    try:
        return dict.get(key, default)
    except:
        return default
