def half(value, toformat=False):
    halfed = value / 2
    if toformat:
        halfed = coin(value / 2)
    return halfed


def duble(value, toformat=False):
    multi = value * 2
    if toformat:
        multi = coin(multi)
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


def resume(value, increase=0, reduction=0):
    print('_' * 29)
    print(f"{'RESUMO DE FUNÇÕES': ^29}|")
    print('_' * 29)
    print(f'Multiplicação: {duble(value, True): >14}|')
    print(f'Divisão: {half(value, True): >20}|')
    print(f'Aumento: {perinc(value, increase, True): >20}|')
    print(f'Redução: {perreduc(value, reduction, True): >20}|')
    print('_' * 29)
