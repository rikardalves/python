def area():
	print(f'{"Área": ^15}')
	print('—' * 15)
	larg = int(input('Largura (m): '))
	height = int(input('Altura (m): '))
	result = f'A área total é de {larg * height}m²'
	return result


print(area())

# Ou

def área(larg, alt):
	r = larg * alt
	print(f'A área total é de {r}m²')


print(f'{"Área": ^15}')
print('—' * 15)
área(int(input('Largura: ')), int(input('Altura: ')))