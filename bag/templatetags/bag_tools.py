# This code is widely adapted from Boutique Ado - Code institute lessons

from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
