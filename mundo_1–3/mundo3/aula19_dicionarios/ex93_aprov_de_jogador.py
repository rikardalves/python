dici = {'jogador' : input('Nome: ').strip().title(),
			'partidas' : int(input('Quantidade de partidas: ')),
			'partida' : []}
for c in range(0, dici['partidas']):
	dici['partida'].append(int(input(f'Número de gols da {c + 1}ª partida: ')))
dici['total'] = sum(dici['partida'])
#Mostragem
print(f'O jogador {dici["jogador"]} jogou {dici["partidas"]} partidas')
for n in range(0, dici['partidas']):
	print(f' ➝ Na {n + 1}ª partida ele fez {dici["partida"][n]} gol(s)')
print(f'Totalizando {dici["total"]} gols')