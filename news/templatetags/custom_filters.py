from django import template
from functools import reduce

register = template.Library()

stop_list = [('дурак', 'д****'), ('Дураки', 'Д*****'), ('дура', 'д***'), ('дуры', 'д***'), ('сука', 'с***'),
             ('суки', 'с***'), ('Кобели', 'К*****'), ('тварей', 'т*****')]

forbidden_words = ['дурак', 'Дураки', 'дура', 'дуры', 'сука', 'суки', 'Кобели', 'тварей']

@register.filter(name='censor')
def currency(value: str):
    return reduce(lambda s, r: s.replace(r[0], r[1]), stop_list, value)

@register.filter
def hide_forbidden(value):
    words = value.split()
    result = []
    for word in words:
        if word in forbidden_words:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)