value = ''
cont = sm = 0
while value != 'parar':
	value = input('Digite os valores aqui ou parar: ').lower().strip().replace(',', '.')
	sep = value.split('.')
	if ''.join(sep).isnumeric() == True or value.isnumeric() == True:
		if cont == 0:
			m = M = float(value)
		sm += float(value)
		cont += 1
		if float(value) < m:
			m = float(value)
		if float(value) > M:
			M = float(value)
	elif value != 'parar':
		print('Desconsiderado')
mid = sm/cont
if sm % 1 != 0 or mid % 1 != 0:
	mid = f'{mid:.1f}'
else:
	mid = int(mid)
if M % 1 == 0:
	M = int(M)
if m % 1 == 0:
	m = int(m)
print(f'A média dos {cont} valores é {mid}, sendo o maior {M} e o menor {m}')
