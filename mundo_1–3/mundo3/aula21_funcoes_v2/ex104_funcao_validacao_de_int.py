def readint(msg):
	while True:
		num = str(input(msg))
		if num.isdecimal():
			num = int(num)
			break
		else:
			print('\033[1;31mErro, digite um número inteiro\033[m')
	return num

n = readint('Digite um número: ')
print('Você digitou o número', n)
