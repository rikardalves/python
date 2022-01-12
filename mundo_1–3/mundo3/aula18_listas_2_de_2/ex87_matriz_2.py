linha = int(input('Número de linhas: '))
coluna = int(input('Número de colunas: '))
matriz = []
sumpar = sum3 = 0
for cont in range(0, 2):
	for l in range(0, linha):
		if cont == 0:
			matriz.append(list())
		for c in range(0, coluna):
			if cont == 0:
				value = int(input(f'Digite o valor da posição [{l}, {c}]: '))
				matriz[l].append(value)
				if value % 2 == 0:
					sumpar += value
			else:
				print(f'[{matriz[l][c]: ^5}]', end=' ')
		if cont == 1:
			print()
			sum3 += matriz[l][c]
print(f'Soma dos valores pares: {sumpar}')
print(f'Soma dos valores da 3ª coluna: {sum3}')
print(f'Maior valor da 2ª coluna: {max(matriz[1])}')