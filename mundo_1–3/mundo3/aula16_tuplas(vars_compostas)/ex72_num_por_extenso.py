while True:
	extense = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
	choice = int(input('Digite um número de 0 a 10: '))
	while choice > 10 or choice < 0:
		choice = int(input('Digitr um dos valores solicitados: '))
	print(extense[choice])
	prgnt = input('Quer continuar? ').strip().upper()[0]
	if prgnt == 'N':
		break
