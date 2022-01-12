'''cont = 0
comp = com = ''
re = ''
verde = '\033[1;32m'
while cont <= 1 or sel != 5:
    sel = int(input(f''''''O que você quer fazer{com}?
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
{comp}''''''))
    if sel > 5:
        print('Digite um valor válido')
    elif sel == 5 and cont == 0:
        print('Essa opção estará disponível desta vez')
    elif sel < 5:
        re = 'sim'
        while re == 'sim' or re != 'não':
            if re == 'sim':
                v1 = float(input('1º valor: '))
                v2 = float(input('2º valor: '))
            re = input('Redigitar valores? ').strip().lower()
            if re == 'sim':
                v1
            if re != 'sim' and re != 'não':
                print('Digite uma resposta válida')
        if sel == 1:
            print (f'{verde}{v1} + {v2} = {v1 + v2}')
        elif sel == 2:
            print (f'{verde}{v1} – {v2} = {v1 - v2}')
        elif sel == 3:
            print (f'{verde}{v1} x {v2} = {v1 * v2}')
        elif sel == 4:
            print (f'{verde}{v1} / {v2} = {v1 / v2}')
    comp, com = '[5] Sair\n', ' agora'
    cont += 1
    print('\033[m:' * 30)
'''
# Outro método

cont = 0
comp = com = ''
re = 'sim'
verde = '\033[1;32m'
sel = 5
while cont <= 1 or sel != 6:
    if sel == 5 and cont != 1:
        v1 = float(input('1º valor: '))
        v2 = float(input('2º valor: '))
    sel = 0
    while sel != 5 and sel != 6:
        sel = int(input(f'''\033[mO que você quer fazer{com}?
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
{comp}'''))
        comp, com = '[5] Redigitar valores\n[6] Sair\n', ' agora'
        if sel == 1:
            print (f'{verde}{v1} + {v2} = {v1 + v2}')
        elif sel == 2:
            print (f'{verde}{v1} – {v2} = {v1 - v2}')
        elif sel == 3:
            print (f'{verde}{v1} x {v2} = {v1 * v2}')
        elif sel == 4:
            print (f'{verde}{v1} / {v2} = {v1 / v2}')
        elif cont == 0 and sel == 5 or cont == 0 and sel == 6:
            print('Opção disponível agora')
        elif sel > 6:
            print('Digitr uma opção válida')
        cont += 1
        print('\033[m_' * 30)
