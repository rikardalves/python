ex = input('Digite a expressão: ')
ex = ex.split()
ex = ''.join(ex)
if ex.count('(') == ex.count(')'):
	print(ex.count('('))
	
#

inpt = input('Digite a expressão: ')
mod = []
for character in inpt:
	if character == '(':
		mod.append(character)
	if character == ')':
		if len(mod) > 0:
			mod.pop()
		else:
			mod.append(character)
			break
if len(mod) == 0:
	print('Expressão válida')
else:
	print('Expressão inválida')