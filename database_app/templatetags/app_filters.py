# coding=utf-8

from django import template


register = template.Library()


@register.filter(name='lookup')
def lookup(h, key):
    try:
        return h[key]
    except KeyError:
        return ""