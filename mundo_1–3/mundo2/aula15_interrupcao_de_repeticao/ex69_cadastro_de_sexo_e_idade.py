c18 = cf20 = masc = 0
cont = 1
while True:
	age = int(input(f'Idade da {cont}ª pessoa: '))
	while True:
		sexo = input(f'Sexo da {cont}ª pessoa: ').strip().lower() [0]
		if sexo in 'f' or sexo in 'm':
			break
		else:
			print('Digite um valor válido')
	prgnt = input('Quer continuar? ').strip().lower() [0]
	while prgnt not in 's' and prgnt not in 'n':
		prgnt = input('Digite um valor válido: ').strip().lower() [0]
	if age >= 18:
		c18 += 1
	if age < 20 and sexo == 'f':
		cf20 += 1
		print('ok')
	if sexo == 'm':
		masc += 1
	cont += 1
	if prgnt == 'n':
		break
print(f'''Há {c18} pessoas maiores de idade;
Há {masc} pessoas do sexo masculino cadastrados;
Há {cf20} pessoas do sexo feminino menores de 20 anos.''')