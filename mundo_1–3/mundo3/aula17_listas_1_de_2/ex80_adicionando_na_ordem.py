listnum = []
for c in range(1, 6):
	num = int(input(f'Digite o {c}º valor: '))
	if c == 1 or num > listnum[len(listnum) - 1]:
		position = len(listnum)
		listnum.append(num)
	else:
		for p, n in enumerate(listnum):
			if num <= n:
				listnum.insert(p, num)
				position = p
				break
	if c == 1:
		print('Primeiro valor adicionado a lista')
	elif position == 0:
		print('Valor adicionado no início da lista')
	elif position == len(listnum) - 1:
		print(f'Valor adicionado ao final da lista(posição {position})')
	else:
		print(f'Valor adicionado na posição {position} da lista')
print(listnum)
