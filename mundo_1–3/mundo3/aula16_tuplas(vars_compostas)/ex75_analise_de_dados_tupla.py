num = (int(input('1º valor: ')), int(input('2º valor: ')), int(input('3º valor: ')), int(input('4º valor: ')), )
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
	print(f'O primeiro valor 3 foi digitado na posição {num.index(9)}')
else:
	print('Não há o valor 3')
cont = 0
for c in num:
	if c % 2 == 0:
		cont += 1
print(f'Há {cont} valores pares')