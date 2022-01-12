quant = int(input('Quantas notas quer calcular (2 a 5)? '))
media = ''
a = ''
if quant == 2:
    n1, n2 = float(input('Primeira nota: ')), float(input('Segunda nota: '))
    media = (n1 + n2) / 2
elif quant == 3:
    n1, n2, n3 = float(input('Primeira nota: ')), float(input('Segunda nota: ')), float(input('Terceira nota: '))
    media = (n1 + n2 + n3) / 3
elif quant == 4:
    n1, n2, n3, n4 = float(input('Primeira nota: ')), float(input(
        'Segunda nota: ')), float(input('Terceira nota: ')), float(input('Quarta nota: '))
    media = (n1 + n2 + n3 + n4) / 4
elif quant == 5:
    n1, n2, n3, n4, n5 = float(input('Primeira nota: ')), float(input(
        'Segunda nota: ')), float(input('Terceira nota: ')), float(input('Quarta nota: ')), float(input('Quinta nota: ')
                                                                                                  )
    media = (n1 + n2 + n3 + n4 + n5) / 5
else:
    print('Digite um valor válido')
if 1 != quant <= 5:
    if media >= 6:
        a = 'Você foi aprovado'
    else:
        a = 'Você está de recuperação'
    print('''Sua media é de {:.1f}
{}'''.format(media, a))
