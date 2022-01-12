matriz = [[], [], []]
for cont in range(0, 2):
	for l in range(0, 3):
		for c in range(0, 3):
			if cont == 0:
				matriz[l].append(int(input(f'Digite o valor da posição [{l}, {c}]: ')))
			else:
				print(f'[{matriz[l][c]: ^5}]', end=' ')
		if cont == 1:
			print()
#Perguntando

linha = int(input('Número de linhas: '))
coluna = int(input('Número de colunas: '))
matriz = []
for cont in range(0, 2):
	for l in range(0, linha):
		if cont == 0:
			matriz.append(list())
		for c in range(0, coluna):
			if cont == 0:
				matriz[l].append(int(input(f'Digite o valor da posição [{l}, {c}]: ')))
			else:
				print(f'[{matriz[l][c]: ^5}]', end=' ')
		if cont == 1:
			print()