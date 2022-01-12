# Última tentativa de redução
t1 = float(input('1º termo da PA: '))
r = float(input('Razão: '))
q = int(input('Quantidade de termos: '))
cont = q
# Looping para printar termos da PA
while q > 0:
    print(f'{t1:.1f}' if t1 % 1 != 0 else int(t1), end='')
    print(', ' if q != 1 else '... ', end='')
    t1 += r
    q -= 1
# Rodada na inclusão do último termo da PA
    if q == 0:
    	prgnt = ''
# Looping caso a "resposta seja inválida"
    	while prgnt != 'não' and prgnt != 'sim':
	    	prgnt = input('\nQuer digitar mais termos? ').strip().lower()
	    	if prgnt == 'sim':
# "q" ficará > 0 e o 1º loop será True novamente
	    		q = int(input('Quantos? '))
	    		cont += q
	    	elif prgnt == 'não':
	    		print(f'Ok, a quantidade total de termos foram de {cont}', end='')
	    	else:
	    		print('Digite uma opção válida', end='')

# 2ª tentativa de redução

#t1 = float(input('1º termo da PA: '))
#r = float(input('Razão: '))
#q  = cont = 0
#prgnt = 'sim'
#while prgnt == 'sim' or prgnt != 'não':
#	if cont == 0:
#		q = int(input('Quantidade de termos: '))
#		cont += q
#	else:
#		prgnt = input('Quer digitar mais termos? ')
#		if prgnt == 'sim':
#			q = int(input('Quantos? '))
#			cont += q
#		elif prgnt == 'não':
#			print(f'Ok, a quantidade total de termos mostrados foram {cont}.')
#		else:
#			print('Digite uma opção válida')
#	while q != 0:
#		if t1 % 1 != 0:
#			a = f'{t1:.1f}'
#		else:
#			a = int(t1)
#		print(a, end='')
#		print(', ' if q != 1 else '... ', end='')
#		t1 += r
#		q -= 1
