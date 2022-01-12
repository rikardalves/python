def half(value):
    a = value / 2
    return a


def duble(value):
    a = value * 2
    return a


def percent(value, percentage):
    a = (percentage / 100) * value
    return a


def coin(valor=0):
    a = str(f'R$ {valor:,.2f}').replace(',', '.')
    a = a[:-3] + ',' + a[-2:]
    return a
