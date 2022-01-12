import calc

value = float(input('Digite um valor em reais: '))
print(f'O dobro de {calc.coin(value)} é {calc.coin(calc.duble(value))}')
print(f'A metade é {calc.coin(calc.half(value))}')
complet = ' '
while True:
    esc = input(f'Quer saber{complet}alguma porcentagem? ').strip().lower()[0]
    if esc == 's':
        percent = int(input('Digite o valor da porcentagem: '))
        print(f'{percent}% de {calc.coin(value)} é {calc.coin(calc.percent(value, percent))}')
        complet = ' mais '
    elif esc == 'n':
        print('Ok')
        break
    else:
        print('digite ao menos "s" ou "n"')
