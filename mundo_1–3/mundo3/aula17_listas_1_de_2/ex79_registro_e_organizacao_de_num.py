listc = list()
while True:
	inpt = input('Digite um valor inteiro ou sair: ').lower().strip()
	if inpt.isdecimal() == True:
		if int(inpt) in listc:
			print('Já existe na lista, desconsiderado')
		else:
			listc.append(int(inpt))
			print('Adicionado')
	elif inpt == 'sair':
		break
	else:
		print('Digite um valor válido')
listc.sort()
print(listc)