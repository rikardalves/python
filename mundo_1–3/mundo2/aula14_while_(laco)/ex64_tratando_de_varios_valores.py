value = sm = cont = 0
while value != 999:
	value = int(input('999 para parar, valor: '))
	if value != 999:
		sm += value
		cont += 1
print(f'A quantidade de números somados foi {cont} e o total foi {sm}')

# Método 2

value, sm, cont = 0, 0, -1
while value != 999:
	sm += value
	cont += 1
	value = int(input('999 para parar, valor: '))
print(f'A quantidade de números somados foi {cont} e o total foi {sm}')

# Método do professor

sm = cont = 0
value = int(input('999 para parar, valor: '))
while value != 999:
	sm += value
	cont += 1
	value = int(input('999 para parar, valor: '))
print(f'A quantidade de números somados foi {cont} e o total foi {sm}')
	