listagem = ('Lápis', 1.5, 'Borracha', 0.75, input('Produto: ').capitalize(), float(input('Valor: ')))
print('—' * 41)
print(f'{"LISTAGEM DE PREÇOS": ^41}|')
print('—' * 41 + '|')
for num, c in enumerate(listagem):
	if num % 2 == 0:
		print(f'{c:.<30}R$', end = '')
	else:
		formatar = f'{listagem[num]:,.2f}'
		a = formatar[:- 4].replace(',', '.') + formatar[- 4:].replace('.', ',')
		print(f"{a: >8} |")
print('—' * 41)