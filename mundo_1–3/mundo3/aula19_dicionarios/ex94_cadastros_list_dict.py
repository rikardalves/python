qntdd = int(input('Número de pessoas a serem cadastradas: '))
add = qntdd
db = list()
med = 0
while True:
	for p in range(0, qntdd):
		print('—' * 41)
		temp = dict()
		temp['nome'] = input('Nome: ').strip().title()
		temp['idade'] = int(input(f'Idade de {temp["nome"]}: '))
		while True:
			temp['sexo'] = input(f'Sexo de {temp["nome"]} (masc, fem ou outro): ').strip().lower()
			if temp['sexo'] not in ('masculino',  'feminino', 'outro', 'masc', 'fem'):
				print('\033[1;31mDigite corretamente\033[m')
			else:
				break
		db.append(temp)
		med += db[p]['idade']
	while True:
		prgnt = input('Quer cadastrar mais pessoas (s/n)? ').strip().lower() [0]
		if prgnt == 's':
			qntdd = int(input('Quantas? '))
			add += qntdd
			break
		elif prgnt == 'n':
			break
		else:
			print('\033[1;31mDigite corretamente\033[m')
	if prgnt == 'n':
		break
# Mostragem
print('—' * 41)
print(f'{add} pessoas foram cadastradas')
print(f' A média de idade é {med/add:.1f}')
print('—' * 22)
print(f'{"Lista de mulheres": ^22}|')
for age in range(0, add):
	if db[age]['sexo'] in ('fem', 'feminino'):
		print(f"{db[age]['nome']: ^22}|")
print('—' * 22)
print(f'{"Idades acima da média": ^22}|')
for age in range(0, add):
	if db[age]['idade'] > med/add:
		print(f"{db[age]['nome']: ^22}|")
print('—' * 22)
