times = ('Palmeiras', 'Atlético-MG', 'Fortaleza EC', 'Bragantino', 'Athletico-PR', 'Flamengo', 'Ceará', 'Atlético Goianiense', 'Bahia', 'Corinthians', 'Fluminense', 'Santos', 'Juventude', 'Internacional', 'Cuiabá', 'Sport', 'São Paulo', 'América-MG', 'Grêmio', 'Chapecoense')
print('—' * 23)
print('Os primeiro 5 colocados')
print('—' * 23)
for quatro in times[:5]:
	print(' ' * ((21 - len(quatro)) // 2), quatro)
print('—' * 23)
#4 colocados
print('\n\033[1mOs últioms 4 colocados são: \033[m', end= '')
for cont5, cinco in enumerate(times[- 4:]):
	print(cinco, end = ', ') if cont5 < 3 else print(f'{cinco}. \n')
#Alfabetico 23 - alfa
print('—' * 36)
for num, alfa in enumerate(sorted(times)):
	print(f'{alfa} {" "  * (23 - len(alfa))}', end = '')
	if num % 2 == 1:
		print('\n')
print('—' * 36)

while True:
	position = input('digite aqui o time que queira saber a posição: ').strip()
	if 'ec' in position.lower() or '-' in position:
		if '-' in position:
			limit = position.find('-')
			position = position[: limit].capitalize(), position[limit + 1:].upper()
			position = '-'.join(position)
		else:
			position = position.split()
			position = position[0].capitalize(), position[1].upper()
			position = ' '.join(position)
	else:
		position = position.title()
	if position not in times:
		print('Digite um valor válido')
	else:
		break
print(times.index(position) + 1)