lista = []
while True:
	inpt = input('Digite um valor ou sair: ').strip().lower()
	if inpt.isdecimal() == True:
		lista.append(int(inpt))
	elif inpt == 'sair':
		break
	else:
		print('Digite um valor válido')
lista.sort(reverse=True)
print(f'A lista contém {len(lista)} elementos')
print(f'{"—" * 26}\nLista em ordem decrescente\n{lista}\n{"—" * 26}')
if 5 in lista:
	print(f'O valor 5 aparece primeiramente na posição {lista.index(5)}')
else:
	print('O valor 5 não aparece na lista')