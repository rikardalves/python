prgnt = int(input('Quqntas pessoas a serem cadastradas? '))
records = []
for a in range(0, prgnt):
	entrada = [input('Digite seu nome: ').title(), float(input('Peso: '))]
	records.append(entrada[:])
print(f'{len(records)} pessoas cadastradas')
men = mai = 0
nomai = list()
nomen = list()
for z in range(0, 2):
	for p, c in enumerate(records):
		if z == 0:
			if p == 0:
				men = mai = c[1]
			else:
				if c[1] > mai:
					mai = c[1]
				elif c[1] < men:
					men = c[1]
		elif z == 1:
			if c[1] == mai:
				nomai.append(c[0])
			elif c[1] == men:
				nomen.append(c[0])
print(f'menor: {men} - {nomen}')
print(f'maior: {mai} - {nomai}')