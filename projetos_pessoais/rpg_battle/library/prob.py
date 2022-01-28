def per(valor, showresult=False):
	"""
	-> Função que define o resultado de uma probabilidade em porceentagem
	Valor sorteado abaixo ou igual ao parâmetro valor retorna True
	Caso contrário retorna False
	:param valor: valor da porcentagem
	:param showresult: mostra o número aleatório sorteado
	:return: valor booleano (True ou False)
	"""
	from random import randint
	random, output = randint(1, 100), False
	for percent in range(1, valor + 1):
		if random == percent:
			output = True
	if showresult:
		print(random, end=' ')
	return output
