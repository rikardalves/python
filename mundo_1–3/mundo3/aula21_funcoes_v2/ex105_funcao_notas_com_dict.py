def notas(*n, sit=False):
	med = 0
	for c in n:
		med += c
	med /= len(n)
	n = {'total':len(n), 'maior':max(n), 'menor':min(n), 'média':med}
	if sit:
		n['situação'] = 'boa'
		if n['média'] < 6:
			n['situação'] = 'ruim'
	return n

resp = notas(5, 8, 5, 6, sit=True)
print(resp)
