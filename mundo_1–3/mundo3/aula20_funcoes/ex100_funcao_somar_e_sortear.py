def sortear(qntdd):
	lista = list()
	from random import randint
	for c in range(0, qntdd):
		lista.append(randint(0, 10))
		lista.sort()
	return lista


def somar(variable, ip):
	b = 0
	for d in variable:
		if ip == 0:
			if d % 2 == 0:
				b += d
		if ip == 1:
			if d % 2 != 0:
				b += d
	if ip not in [0, 1]:
			print('0 para par e 1 para ímpar')
	else:
		return b


a = sortear(6)
print(a)
print(somar(a, 0))