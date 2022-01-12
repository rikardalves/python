db = list()
while True:
	dici = {'jogador' : input('Nome: ').strip().title(),
				'partidas' : int(input('Quantidade de partidas: ')),
				'partida' : []}
	for c in range(0, dici['partidas']):
		dici['partida'].append(int(input(f'Número de gols da {c + 1}ª partida: ')))
	dici['total'] = sum(dici['partida'])
	db.append(dici)
	while True:
		prgnt = input('Adicionar outro? (S/N): ').strip().upper()[0]
		if prgnt in ('N', 'S'):
			break
		else:
			print('Digite corretamente')
	if prgnt == 'N':
		break
#Mostragem
print(' ' + '—' * 42)
print('|  №  |Jogador(a) |    Partidas    | Total |')
print(' ' + '—' * 42)
for n, j in enumerate(db):
	print(f'|{n: ^5}|{j["jogador"]: ^11}|{str(j["partida"]): ^16}|{j["total"]: ^7}|')
print(' ' + '—' * 42)
while True:
	detail = input('Detalhe do jogador: ').strip().lower().replace('ã', 'a')
	if detail.isdecimal() == True:
		detail = int(detail)
		if detail > len(db) - 1 or detail < 0:
			print('Este número não está atribuído a nenhum jogador')
		else:
			print(f'\033[1mO jogador {db[detail]["jogador"]} jogou {db[detail]["partidas"]} partidas\033[m')
			for n in range(0, db[detail]['partidas']):
				print(f' ➝ Na {n + 1}ª partida ele fez {db[detail]["partida"][n]} gol(s)')
			print(f'   \033[1;32mTotalizando {db[detail]["total"]} gol(s)\033[m')
	elif detail == 'nao':
		break
	else:
		print('Digite corretamente')
