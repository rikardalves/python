def regis(nome='', gols=''):
	nome = str(nome)
	gols = str(gols)
	if nome == '' or nome.isnumeric() == True:
		name = 'desconhecido'
	else:
		name = nome.title()
	if gols.isdecimal() == False:
		gols = 0
	else:
		gols = int(gols)
	if gols == 1:
		comp = ''
	else:
		comp = 's'
	conc = f'O jogador {name} fez {gols} gol{comp}'
	return conc

a = input('Nome do jogador: ')
b = input('Quantidade de gols: ')
print(regis(a, b))