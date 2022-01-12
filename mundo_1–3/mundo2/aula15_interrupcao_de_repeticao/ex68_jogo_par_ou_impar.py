from random import randint
from calc.prob import per
'''
cont = 0
while True:
	ch = int(input('Digite um número de 1 a 10: '))
	ran = randint(1, 10)
	sel = ' '
	while 'i' not in sel not in 'p':
		sel = input('Par ou ímpar? ').strip().lower().replace('í', 'i') [0]
		r = (ch + ran) % 2
	if sel == 'i' and r != 0 or sel == 'p' and r == 0:
		print(f'Eu escolhi {ran}. Total de {ch + ran}, você ganhou!')
		cont += 1
	else:
		print(f'Eu escolhi {ran}. Total de {ch + ran}, você perdeu!')
		break
comp = ''
if cont != 1:
	comp = 'es'
print(f'Você venceu {cont} vez{comp}')
'''
# Me

cont = save = 0
value = 0
while True:
	aviso = per(value)
	sel = ' '
	while sel [0] not in ('p', 'i', 's'):
		sel = input('Par, ímpar ou sair? ').strip().lower().replace('í', 'i')
		print('_' * (20 + len(sel)))
	if sel == 's':
		break
	print(' ' * 7 + 'NÚMEROS\n' + '_' * (20 + len(sel)))
	ch = int(input('Digite um número de 1 a 10: '))
	ran = randint(1, 10)
	r = (ch + ran) % 2
	if sel [0] == 'i' and r != 0 or sel [0] == 'p' and r == 0:
		print(f'Eu escolhi {ran}. Total de {ch + ran}, você ganhou!')
		cont += 1
		value += 1
		if save < cont:
			save = cont
	else:
		print(f'Eu escolhi {ran}. Total de {ch + ran}, você perdeu!')
		cont = 0
	if aviso == 1:
		print('\033[31mJá estou ficando cansado')
comp = ''
if cont != 1:
	comp = 'es'
print(f'O maior número de vitórias subsequentes foram de {save} vez{comp}')