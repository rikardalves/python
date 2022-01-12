from random import randint
num = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print('—' * 16)
print('LISTA DE NÚMEROS')
print('—' * 16)
for n in num:
	print(' ' * ((14 - len(str(n)))//2), n)
print('—' * 16)
print(f'O maior número é {max(num)}, e o menor é {min(num)}')