while True:
	num = int(input('Digite o valor para saber sua tabuada (0 encerra): '))
	print('_' * 50)
	for c in range(1, 11):
		if c == 3 or c == 6 or c == 9:
			a = '\n'
		else:
			a = ''
		print(f'{num} x {c} = {num * c} | {a}', end='')
	print('\n' + '_' * 50 + '\n')
	if num == 0:
		break

# Formatado em lista

while True:
	num = int(input('Digite o valor para saber sua tabuada (0 encerra): '))
	print('_' * 48)
	for c in range(1, 11):
		print(f'{num} x {c} = {num * c}')
	print('_' * 48 + '\n')
	if num == 0:
		break
