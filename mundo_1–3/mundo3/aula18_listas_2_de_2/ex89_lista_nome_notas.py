qnt = int(input('Número de alunos: '))
db = []
for a in range(0, qnt):
	db.append([])
	db[a].append(input('Nome: ').strip().title())
	db[a].append(float(input('1ª nota: ')))
	db[a].append(float(input('2ª nota: ')))
db.sort()
print('—' * 27)
print('nº Nome             Média')
print('—' * 27)
for z in range(0, 2):
	for q in range(0, qnt):
		if z == 0:
			db[q].insert(0, q + 1)
		else:
			print(db[q][0], end='  ')
			print(f'{db[q][1]: <18}', end='')
			print(f'{(db[q][2] + db[q][3])/2: ^5.1f}')
print('—' * 27)
while True:
	search = input('Procurar por número: ').strip().lower().replace('ã', 'a')
	if search.isdecimal() == True:
		if int(search) > db[len(db) - 1][0] or int(search) < 1:
			print('Não há este valor na lista')
		else:
			lct = db[int(search) - 1]
			print(f'Nome: {lct[1]} | Notas: {lct[2]} e {lct[3]}')
	elif search == 'nao':
		break
	else:
		print('Inválido')
