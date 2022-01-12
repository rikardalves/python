from random import randint
from operator import itemgetter
players = {'jogador 1' : '', 
				  'jogador 2' : '', 
				  'jogador 3' : '', 
				  'jogador 4' : ''}
for c in players.keys():
	players[c] = randint(1, 6)
players = sorted(players.items(), key=itemgetter(1), reverse=True)
print(players)
for p, v in enumerate(players):
	print(f'{p + 1}º lugar: {v[0]}, obteve o resultado {v[1]}')
