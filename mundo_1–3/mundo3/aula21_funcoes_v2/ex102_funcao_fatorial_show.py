def fatorial(num, show=False):
	f = 1
	for c in range(num, 0, -1):
		if show:
			print(c, end=' ')
			if c >1:
				print('x', end=' ')
			else:
				print('=', end=' ')
		f *= c
	return f

def comb(p, n):
	c = 1
	l = 1
	for a in range(p, n - 1, -1):
		c *= a
	for b in range(n, 0, - 1):
		l *= b
	t = int(c/l)
	return t


print(comb(5, 3))
print(fatorial(5))
