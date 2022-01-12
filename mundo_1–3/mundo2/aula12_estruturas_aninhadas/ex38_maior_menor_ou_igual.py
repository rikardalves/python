num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
calc, calc2 = '', ''
if num1 < num2:
    calc, calc2 = 'menor', 'maior'
elif num1 > num2:
    calc, calc2 = 'maior', 'menor'
if num1 != num2:
    print(f'O primeiro número é o {calc}')
    print(f'O segundo número é o {calc2}')
else:
    print('Os dois números são iguais')
# Método 2
n1 = int(input('n1: '))
n2 = int(input('n2: '))
r = 'menor'
if n1 > n2:
    r = 'maior'
if n1 != n2:
    print(f'O primeiro número é o {r}')
else:
    print('Iguais')
