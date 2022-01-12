acum, cont = 0, 0
for c in range(0, 6):
    a = int(input('Digite um número inteiro: '))
    if a % 2 == 0:
        acum += a
        cont += 1
if cont == 1:
    print(f'Há apenas 1 valor par: {acum}')
else:
    print(f'A soma dos {cont} números pares é {acum}')
