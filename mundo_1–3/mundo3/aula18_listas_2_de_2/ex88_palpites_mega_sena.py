from random import randint
qnt = int(input('Número de jogos: '))
games = []
for g in range(0, qnt):
	games.append([])
	p = games[g]
	while len(p) < 6:
		rndm = randint(1, 60)
		if rndm not in p:
			p.append(rndm)
	p.sort()
	print(f'{g + 1}º jogo: {p}')