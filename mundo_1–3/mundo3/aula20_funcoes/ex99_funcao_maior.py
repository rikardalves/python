def maior(*num):
	if num == ():
		print('Não há valores inseridos')
	else:
		print(f'Os {len(num)} valores foram: ', end='')
		for n, c in enumerate (num):
			if n <= len(num) - 2:
				print(c, end=', ')
		print(num[len(num) - 1])
		print(f'O maior valor foi {max(num)}')
	print('—' * 46)

maior()
maior(8, 2, 107, 24, 2973, 12)
