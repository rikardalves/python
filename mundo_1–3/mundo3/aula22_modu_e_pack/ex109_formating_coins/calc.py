def half(value, toformat=False):
    halfed = value / 2
    if toformat:
        halfed = coin(value / 2)
    return halfed


def duble(value, toformat=False):
    multi = value * 2
    if toformat:
        multi = coin(value * 2)
    return multi


def perinc(value, percentage, toformat=False):
    per = ((percentage / 100) * value) + value
    if toformat:
        per = coin(per)
    return per


def perreduc(value, percentage, toformat=False):
    per = value - ((percentage / 100) * value)
    if toformat:
        per = coin(per)
    return per


def coin(valor=0):
    form = str(f'R${valor:,.2f}').replace(',', '.')
    form = form[:-3] + ',' + form[-2:]
    return form
