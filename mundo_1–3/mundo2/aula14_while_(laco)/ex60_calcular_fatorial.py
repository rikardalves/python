fat = int(input('Digite um valor para saber seu fatorial: '))
print(f'O resultado de {fat}! = ', end='')
print('1' if fat == 0 else '', end='')
a = 1
b = ''
while fat > 0:
	a *= fat
	b += str(fat) + ' x '
	fat -= 1
print(f'{b[:len(b) - 3]} é {a}')

# método 2

from math import 	factorial
n = int(input('Valor: '))
f = factorial(n)
print(f'O resultado de {n}! = ', end='')
while n != 0:
    print(f'{n} ', end='')
    print('x' if n != 1 else '=', end=' ')
    n -= 1
print(f)

# Extra com for

fac = int(input('Valor aqui: '))
print('1' if fac == 0 else '', end='')
a = 1
for c in range(fac, 0, -1):
    print(f'{c} ', end='')
    print('x ' if c != 1 else f'= {a}', end='')
    a *= c

# método 2 Extra

fact = int(input('\nValor aqui: '))
for z in range(fact, 0, -1):
    print(f'{z} ', end='')
    print('x ' if z != 1 else f'= {factorial(fact)}', end='')
    