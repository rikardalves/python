value = int(input('Digite o valor que deseja sacar: R$'))
contced = cont = 0
notes = [50, 20, 10, 1]
while True:
	while True:
		if value - notes[cont] < 0:
			if contced > 0:
				print(f'Notas de {notes[cont]}: {contced}')
				contced = 0
			break
		value -= notes[cont]
		contced += 1
	cont += 1
	if cont == 4:
		break
