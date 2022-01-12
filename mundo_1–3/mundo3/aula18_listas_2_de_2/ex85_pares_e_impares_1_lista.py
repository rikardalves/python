lista = [[], []]
for c in range(1, 8):
	value = int(input(f'Digite o {c}º valor: '))
	if value % 2 == 0:
		lista[0].append(value)
		lista[0].sort()
	else:
		lista[1].append(value)
		lista[1].sort()
print(f'Os valores pares são: {lista[0]}')
print(f'Os valores ímpares são: {lista[1]}')
