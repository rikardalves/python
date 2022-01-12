def voto(ano=-1):
	"""Exigido um parâmetro decimal (idade)"""
	from datetime import date
	ano = date.today().year - int(input())
	if ano < 0:
		estado = 'Parâmetro inválido'
	elif ano < 16:
		estado = 'Negado'
	elif ano < 18:
		estado = 'Opcional'
	else:
		estado = 'Obrigatório'
	return estado

help(voto)
print(voto.__doc__)
print(voto(2005))
print(voto(2000))