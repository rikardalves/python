def contador(ini, fim, pul):
	from time import sleep
	if ini > fim:
		pul = -pul
		fim -= 2
	if pul == 0:
		pul = 1
	for c in range(ini, fim + 1, pul):
		print(c, end=' ', flush=True)
		sleep(0.2)
	print()

contador(1, 10, 1)
contador(10, 0, 2)
print('—' * 20)
print('Digite da sua forma')
print('—' * 20)
init = int(input('Valor inicial: '))
final = int(input('Valor final: '))
pulo = int(input('Sequêcia de contagem: '))
contador(init, final, pulo)