limit = float(input('Valor limite para gastar em suas compras: R$ '))
print('''Ok, digite a quantidade, nome e valor dos produtos que irá comprar abaixo (quantidade nome - valor)
Digite "finalizar" para parar''')
soma = price = 0
maior = '0 '
esp = maior.find(' ') + 1
quant = valor = 0, ''
lista = ''
qntvlr = ''
while True:
	pro = str(input('')).strip().replace(',', '.')
	if pro.count(' ') < 3 or ' - ' not in pro or pro[:pro.find(' ')].isnumeric == False or pro[len(pro) - 1].isnumeric == False:
		if pro.lower() == 'finalizar':
			break
		print('\033[1;31mDesconsiderado\033[m')
	else:
		if int(pro[:pro.find(' ')]) > int(maior[:esp]):
			maior = pro
		value = pro[pro.find('$') + 1:]
		value = float(value[value.rfind(' ') + 1:])
		soma += value * int(pro[:pro.find(' ')])
		name = maior[esp : maior.find("-") - 1]
		lista += pro[esp : pro.find("-") - 1].strip() + '\n'
		qntvlr += str(value) + '\n'
		if int(maior[: esp]) > quant[0]:
			quant = int(maior[: esp]), name
		if value > float(valor[0]):
			valor = value, name
		if 's' in name[len(name) - 1]:
			sinplu = 'são os(as)'
		else:
			sinplu = 'é o(a)'
		if price < value:
			price = value
			nopro = pro[esp : pro.find("-") - 1].strip()
if soma > limit:
	print(f'Suas compras excedem R${soma - limit:.2f} do planejado')
	print(f'O produto com maior quantidade {sinplu} {name}({maior[: esp].strip()} unidades)')
	print(f'O produto mais caro vale R${price:.2f}({nopro})')
	while True:
		prgnt = input('Deseja retirar algo? ').strip().lower()
		if prgnt == 'sim':
			print('Ok, digite a quantidade e o produto que quer retirar')
			while True:
				rmv = input('').strip()
				if rmv.lower() == 'ok':
					break
				vlr = qntvlr
				position = int(lista[:lista.find(rmv[rmv.find(' ') + 1 :])].count('\n'))
				while position > 0:
					vlr = vlr.split(vlr[:vlr.find('\n') + 1])
					vlr = str(vlr[1])
					position -= 1
				soma -= int(rmv[:rmv.find(' ')]) * float(vlr[vlr.find(' ') + 1 : vlr.find('\n')])
				print(f'O total é R${soma:.2f}')
			break
		elif prgnt.replace('a', 'ã') == 'não':
			break
		else:
			print('Digite um valor válido')
else:
	print(f'O total de suas compras foi de R${soma:.2f}')
	