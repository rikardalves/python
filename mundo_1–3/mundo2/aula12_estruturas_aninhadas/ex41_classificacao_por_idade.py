from datetime import date, datetime
nome = input('Digite seu nome completo: ').strip().title()
ano = int(input('Ano de nascimento: '))
cal = date.today().year - ano
cat = 'MASTER'
if cal <= 9:
    cat = 'MIRIM'
elif cal <= 14:
    cat = 'INFANTIL'
elif cal <= 19:
    cat = 'JUNIOR'
elif cal <= 25:
    cat = 'SÊNIOR'
da = date.today()
data = datetime.now()
print('''Nome: {}
Data de comparecimento: {}
Categoria: {}'''.format(nome, data.strftime('%d/%m/%Y às %H:%M:%S'), cat))
