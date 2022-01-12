num = int(input('Digite um número para saber se é primo: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;31m', end='')
        cont += 1
    else:
        print('\033[1;34m', end='')
    print(c, end=' ')
if num != 1:
    p = 's'
else:
    p = ''
print(f'\n\033[mO número {num} é divisível por {cont} número{p} (vermelho{p})')
if cont == 2:
    print('Sendo assim, ele é primo')
else:
    print('Sendo assim, ele não é primo')
