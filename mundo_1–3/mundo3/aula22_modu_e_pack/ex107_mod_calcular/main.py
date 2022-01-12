import calc

value = float(input('Digite um valor em reais: '))
print(f'O dobro de R${value:.2f} é R${calc.duble(value):.2f}')
print(f'A metade é R${calc.half(value):.2f}')
complet = ' '
while True:
    esc = input(f'Quer saber{complet}alguma porcentagem? ').strip().lower()[0]
    if esc == 's':
        percent = int(input('Digite o valor da porcentagem: '))
        print(f'{percent}% de {value:.2f} é {calc.percent(value, percent):.2f}')
        complet = ' mais '
    elif esc == 'n':
        print('Ok')
        break
    else:
        print('digite ao menos "s" ou "n"')
