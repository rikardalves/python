import calc

value = float(input('Digite um valor em reais: R$'))
print(f'O dobro de {calc.coin(value)} é {calc.duble(value, 1)}')
print(f'A metade é {calc.half(value, 1)}')
complet = ' '
while True:
    esc = input(f'Quer saber{complet}algum o aumento ou redução em porcentagem? ').strip().lower()[0]
    if esc == 's':
        choic = int(input('[1] Aumento\n[2] Redução\n'))
        # Ação para cada escolha
        if choic == 1:
            incre = int(input('Porcentagem: '))
            print(f'O aumento de {incre}% de {calc.coin(value)} é {calc.perinc(value, incre, 1)}')
        elif choic == 2:
            reduc = int(input('Porcentagem: '))
            print(f'A redução de {reduc}% de {calc.coin(value)} é {calc.perreduc(value, reduc, 1)}')
        else:
            print('Digite um valor válido')
    elif esc == 'n':
        print('Ok')
        break
    else:
        print('digite ao menos "s" ou "n"')