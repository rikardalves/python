from datetime import datetime
y = datetime.now().year
m = datetime.now().month
db = {'nome' : input('Nome: ').strip().title(),
		  'idade' : y - int(input('Ano de nascimento: '))}
if db['idade'] >= 18:
	while True:
		db['CTPS'] = input('CTPS(nº-série): ').strip().lower()
		if '-' in db['CTPS'] and db['CTPS'].replace('-', '').isnumeric():
			if len(db['CTPS']) == 12 and db['CTPS'][7] == '-':
				break
			else:
				print('\033[1;31mInválido\033[m')
		elif db['CTPS'].replace('ã', 'a') in 'nao tenho':
			del db['CTPS']
			break
		else:
			print('\033[1;31mInválido\033[m')
if 'CTPS' in db:
	db['contratação'] = int(input('Ano de contratação: ')) - (y - db['idade'])
	db['salário'] = float(input('Salário: '))
	db['aposentadoria'] = db['contratação'] + 20 if db['contratação'] >= 45 else 65
for k, v in db.items():
	print(f'A chave {k} tem valor {v}')