from random import randint
def per(valor):
	a, b = randint(1,100), False
	for c in range(1, valor + 1):
		if a == c or valor > 100:
			b = True
	return b
