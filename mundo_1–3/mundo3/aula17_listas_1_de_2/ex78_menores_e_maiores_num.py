lista = []
for num in range(1, 6):
	lista.append(int(input(f'Digite o {num}º número: ')))
pl = []
ps = []
for p, v in enumerate(lista):
	if v == max(lista):
		pl.append(str(p + 1))
	if v == min(lista):
		ps.append(str(p + 1))
print(f"O maior valor corresponde a {max(lista)}, situado na(s) posição(ões): {', '.join(pl)}")
print(f"O menor valor corresponde a {min(lista)}, situado na(s) posição(ões): {', '.join(ps)}")
