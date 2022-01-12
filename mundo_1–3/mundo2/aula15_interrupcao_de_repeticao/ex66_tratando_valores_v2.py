sm = cont = 0
while True:
	value = int(input('999 para parar, valor: '))
	if value == 999:
		break
	sm += value
	cont += 1
print(f'A soma dos {cont} valores é {sm}')

# Com parar

su = cntd = 0
while True:
	val = input('Valor ou parar: ').strip().lower()
	if val.isnumeric() == True:
		val = int(val)
		cntd += 1
		su += val
	if val == 'parar':
		break
print(f'A soma dos {cntd} valores é {su}')
