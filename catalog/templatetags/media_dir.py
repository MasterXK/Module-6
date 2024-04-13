from django import template


register = template.Library()


@register.filter()
def media_dir(data):
    if data:
        return f'/media/catalog/{data}'
    return '#'
