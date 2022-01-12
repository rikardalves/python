from datetime import date
cont = 0
anos = ''
for c in range(1, 7):
    idade = int(input(f'Coloque aqui o {c}º ano de nascimento: '))
    anos += str(date.today().year - idade) + ', '
    if date.today().year - idade >= 18:
        cont += 1
if cont == 1:
    a, b = 'pessoa é maior de idade', 'pessoas são menores de idade'
elif c - cont == 1:
    a, b = 'pessoas são maoiores de idade', 'pessoa é menor idade de idade'
else:
    a, b = 'pessoas são maoiores de idade', 'pessoas são menores de idade'
print(f'''As idades são, respectivamente: {anos[:len(anos) - 2]}
{cont} {a} e {c - cont} {b}''')
