lista = list()
imp = []
par = []
prgnt = int(input('Digite a quantidade de valores que deseja adicionar: ')) + 1
for c in range(1, prgnt):
	lista.append(int(input(f'Digite o {c}º valor: ')))
lista.sort()
for v in lista:
	if v % 2 == 0:
		par.append(v)
	else:
		imp.append(v)
print(f'Lista completa: {lista}')
print(f'Lista de pares: {par}\nLista de ímpares: {imp}')
