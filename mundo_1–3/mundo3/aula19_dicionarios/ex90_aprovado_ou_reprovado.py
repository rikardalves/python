dici = {'nome' : input('Seu nome: ').strip().title(),
			'média' : float(input('Sua média: '))
			}
if dici['média'] < 3:
	dici['stiuação'] = 'reprovado'
elif dici['média'] >= 6:
	dici['situação'] = 'aprovado'
else:
	dici['situação'] = 'recuperação'
for k, v in dici.items():
	print('O' if k == 'nome' else 'A', end=' ')
	print(f'{k} do aluno é {v}')