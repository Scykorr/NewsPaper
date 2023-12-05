from django import template
from functools import reduce

register = template.Library()

stop_list = [('дурак', 'д****'), ('Дураки', 'Д*****'), ('дура', 'д***'), ('дуры', 'д***'), ('сука', 'с***'),
             ('суки', 'с***'), ('Кобели', 'К*****'), ('тварей', 'т*****')]


@register.filter(name='censor')
def currency(value: str):
    return reduce(lambda s, r: s.replace(r[0], r[1]), stop_list, value)
