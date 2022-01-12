from random import choice, shuffle
from prob import per

def spotar(spot):
	d = e = 0
	actif = 0
	for spo in range(spot - 5, spot + 6):
		if spo in dark:
			if d == 0:
				if spo > spot:
					d = 1
					actif += 1
					print('Tem na direita')
			if e == 0:
				if spo < spot:
					actif += 1
					e = 1
					print('Tem na esquerda')
		elif actif == 0 and spo == spot + 5:
			print('Tudo limpo aos arredores')
	return spot


def spotlist(sp):
	d = e = 0
	right = left = 'Seguro'
	for spo in range(sp - 5, sp + 6):
		if spo in dark:
			if d == 0:
				if spo > sp:
					d = 1
					right='Perigo'
			if e == 0:
				if spo < sp:
					e = 1
					left='Perigo'
	s = f'{left} •{sp}• {right}'
	return s


def blocos():
	first, final, space = 1, 34, 0
	txt = ''
	for z in range(1, 4):
		for tabela in range(first, final):
			if tabela in dark:
				space += 1
		txt += f'Bloco({first} — {final - 1}): '
		if z == 1:
			azar = choice([1, 2, 3])
		if azar == z:
			txt += '?\n'
		elif 0 <= space <= 1:
			txt += '0 ou 1\n'
		elif 2 <= space <= 3:
			txt += '2 ou 3\n'
		elif 4 <= space <= 5:
			txt += '4 ou 5\n'
		if z == 2:
			final += 1
		first += 33
		final += 33
		space = 0
	return txt


def line(num, var=False, bar=False):
	if bar:
		bar = '|'
	else:
		bar = ' '
	if var:
		print(f'{bar}{"—" * len(num)}{bar}{reset}')
	else:
		print(f'{bar}{"—" * num}{bar}{reset}')


def ent(num):
	for ente in range(0, num):
		print()


def ficha():
	if len(str(db[cont]["Coin"])) == 1:
		y, x = 7, 6
	else:
		y, x = 6, 6
	ent(14)
	line(20)
	print(f'|{db[cont]["Cor"]}{db[cont]["Name"]:▂^18}▂▂{reset}|')
	line(20, 0, 1)
	print(f'|{" "*y}{db[cont]["Coin"]} x 🟡 {" "*x}{reset}|')
	print(f'|{" "*7}{db[cont]["Life"]} x ♥️ {" "*6}{reset}|')
	print(f'|{" "*7}{db[cont]["Limitbloc"].conjugate()} x ➗ {" "*6}{reset}|')
	line(20)

reset='\033[m'
lista = []
dark = []
vivo = ['Vivo(a)... por enquanto', 'Já está se sentindo cheio(a)?', 'Só mais uma...', 'Vou querer uma parte da grana', 'Queria ter essa sorte', 'Sua ganância é preocupante', 'Ainda quer arriscar mais?', 'Qual o preço da sua vida mesmo?', 'Bem que falam que gato tem 7 vidas', 'Mais uma e não se fala mais nisso', 'Me questiono sobre sua sanidade']
morto = ['Rest in piece ;-;', 'Finalmente verá se no céu tem pão', '1 vida a menos, um milionário a mais', 'Vou contar pra sua mãe', 'Se sua mãe souber disso ela te mata', 'Morreu...']
players = list()
db = []
bs = [2, 3]
cor = 30


qntdd = int(input('Número de jogadores: '))
for bi in range(0, 2):
	for person in range(0, qntdd):
		if bi == 0:
			players.append(input(f'Nome do {person + 1}º player: ').title())
			db.append(dict())
			db[person]['Coin'] = 0
			db[person]['Life'] = 1
			db[person]['Limitlife'] = False
			db[person]['3_blocos'] = False
			db[person]['Spot'] = [0, 0, 0, 0]
			db[person]['Limitbloc'] = False
		else:
			if person == qntdd - 1:
				lig = '\n'
			else:
				lig = ', '
			if person == 0:
				shuffle(players)
				ent(41)
				line(20)
				print(f'|{"ORDEM": ^20}|')
				line(20, 0, 1)
			db[person]['Cor'] = f'\033[1;{cor}m'
			cor += 1
			db[person]['Name'] = players[person - 1]
			print(f"|{players[person - 1]: ^20}|")
line(20)
print('—' * 54)


for c in range(1, 101):
	lista.append(c)


for b in range(0, 5):
	while True:
		a = choice(lista)
		if a not in dark:
			dark.append(a)
			break
#print(dark)


cont = 0
for repit in range(0, 100):
	if repit != 0:
		input()
		ent(28)
		print('—' * 53)
	for candy in range(1, 101):
		if candy in lista:
			print(f'{candy}', end=' ')
		else:
			if candy in dark:
				print(f'\033[1;7;31m{candy}{reset}', end=' ')
			else:
				print(f'\033[1;7m{candy}{reset}', end=' ')
		if db[cont]['Limitbloc']:
			if candy == 33 or candy == 66:
				print('\033[1;36m|', reset, end='')
			if candy == 100:
				print()
				print('—' * 54)
				print(blocos(), end='')
	if db[cont]['Limitbloc'] == False:
		print()
	print('—' * 54)
	ficha()
	if db[cont]['Spot'][0] > 0:
		line(20)
		print(f'|{"Lista de spots": ^20}|')
		line(20, 0, 1)
		print(f'|{spotlist(db[cont]["Spot"][1]): ^20}|')
		if db[cont]['Spot'][2] > 0:
			print(f'|{spotlist(db[cont]["Spot"][2]): ^20}|')
		if db[cont]['Spot'][3] > 0:
			print(f'|{spotlist(db[cont]["Spot"][3]): ^20}|')
		line(20)
	while True:
		esc = input('Escolha: ').strip().lower()
		if esc == 'loja':
			print('[1] Vida — Custo: 12 — Estoque: Único')
			print(f'[2] Spotar (campo de 10) — Custo: 8 — Estoque: {bs[1]}')
			print(f'[3] 3 Blocos — Custo: 6 — Estoque: {bs[0]}')
			loja = int(input())
			if loja == 1 and db[cont]['Limitlife'] == False:
				if db[cont]['Coin'] >= 12:
					db[cont]['Life'] = 2
					db[cont]['Limitlife'] = True
					db[cont]['Coin'] -= 12
					print(f'Moedas atuais: {db[cont]["Coin"]}')
				else:
					print('\033[1;33mSem moedas suficientes', reset)
			elif loja == 2:
				if db[cont]['Coin'] >= 8 and bs[1] > 0:
					db[cont]['Coin'] -= 8
					bs[1] -= 1
					db[cont]['Spot'][0] += 1
					db[cont]['Spot'][db[cont]['Spot'][0]] = spotar(int(input('Valor central: ')))
					print(f'Moedas atuais: {db[cont]["Coin"]}')
				elif bs[1] <= 0:
					print('\033[1mJá esgotou o estoque desse bônus', reset)
				else:
					print('\033[1;33mSem moedas suficientes', reset)
			elif loja == 3:
				if db[cont]['Coin'] >= 6 and bs[0] > 0:
					if db[cont]['Limitbloc'] == False:
						print(blocos())
						bs[0] -= 1
						db[cont]['Limitbloc'] = True
					elif db[cont]['Limitbloc']:
						print('Comprou um bônus não interativo pela 2ª vez')
					db[cont]['Coin'] -= 6
					print(f'Moedas atuais: {db[cont]["Coin"]}')
				elif bs[0] <= 0:
					print('\033[1mJá esgotou o estoque desse bônus', reset)
				else:
					print('\033[1;33mSem moedas suficientes', reset)
			#print(db)

		elif esc.isdecimal():
			esc = int(esc)
			if esc > 100 or esc <= 0:
				print('\033[1mEstá pedindo demais', reset)
			elif esc not in lista:
				print('\033[1;36mAlguém já está digerindo esta', reset)
			else:
				break
	lista.remove(esc)
	if esc in dark:
		db[cont]['Life'] -= 1
		if db[cont]['Life'] <= 0:
			print(f'\033[1;31m{choice(morto)}{reset}')
			del db[cont]
			del players[cont]
		else:
			print(f'\033[1;31mPerdeu 1 vida, resta {db[cont]["Life"]}{reset}')
			cont += 1
		if cont > len(db) - 1:
			cont = 0
	else:
		if per(20) == True:	
			temp = choice(vivo)
		else:
			temp = 'Vivo(a)'
		print(f'\033[1;32m{temp}{reset}')
		db[cont]['Coin'] += 2
		#print(db)
		if cont >= len(db) - 1:
			cont = 0
		else:
			cont += 1
	input()
	count = 0
	ent(30)
	line(8 * (len(db) + 1) + len(db))
	for cou in range(0, 5):
		for coun in range(0, len(db)):
			estado = ''
			if cou == 0:
				if coun == 0:
					estado = '|  \033[1mNome\033[m  '
					print(estado, end='')
				print(f"|{db[coun]['Cor']}{db[coun]['Name']: ^8}\033[m", end='')
				if coun == len(db) - 1:
					print('|', end='')
			if cou == 1:
				if coun == 0:
					estado = '| \033[1;33mMoedas\033[m '
					print(estado, end='')
				print(f"|{db[coun]['Coin']: ^8}", end='')
				if coun == len(db) - 1:
					print('|', end='')
			if cou == 2:
				if coun == 0:
					estado = '|  \033[1;31mVida\033[m  '
					print(estado, end='')
				print(f"|{db[coun]['Life']: ^8}", end='')
				if coun == len(db) - 1:
					print('|', end='')
			if cou == 3:
				if coun == 0:
					estado = '| \033[1;36mBlocos\033[m '
					print(estado, end='')
				print(f"|{db[coun]['Limitbloc']: ^8}", end='')
				if coun == len(db) - 1:
					print('|', end='')
			if cou == 4:
				if coun == 0:
					estado = '|  \033[1;32mSpot\033[m  '
					print(estado, end='')
				print(f"|{db[coun]['Spot'][0]: ^8}", end='')
				if coun == len(db) - 1:
					print('|', end='')
		print()
		if cou == 4:
			line(8 * (len(db) + 1) + len(db))
		else:
			print(f"{'|————————' * (len(db) + 1)}|")
		count += 1
	ent(25)