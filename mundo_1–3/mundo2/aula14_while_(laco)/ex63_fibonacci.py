c = '\033[m'
esc = 0
while 2 != esc != 1:
	esc = int(input('''[ 1 ] Modo história
[ 2 ] Fase
\033[36;1m'''))
	if 2 != esc != 1:
		print(f'\033[31;1mDigite uma opção válida{c}')
a = 'Até ' if esc == 1 else ''
t = int(input(c + f'{a}qual termo você quer saber? '.capitalize())) - 2
n1, n2 = 0, 1
if t >= - 1:
	print('' if esc == 2 and t >= 0 else f'{n1}', end='')
print(n2 if esc == 2 and t == 0 else '', end='')
print(f', {n2}' if esc == 1 and t >= 0 else '', end='')
while t > 0:
	seq = n1 + n2
	n1 = n2
	n2 = seq
	if esc == 2 and t == 1:
		print(f'{seq:,}'.replace(',', '.'))
	elif esc == 1:
		print(', ' + f'{seq:,}'.replace(',', '.'), end='')
	t -= 1
'''
La jugada de lo mestre
Quebra de e junção de linha
print('\033[31;1mDigite uma opção válida\033[m\n' if 2 != esc != 1 else '', end='')
'''
