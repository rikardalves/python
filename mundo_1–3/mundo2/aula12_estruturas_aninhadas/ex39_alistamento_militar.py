idade = int(input('quantos anos você tem? '))
a = ''
if idade < 18:
    print('Anda não está na hora')
    a = 'Você deverá se alistar daqui {} anos'.format(18 - idade)
elif idade > 21:
    print('Já passou da hora!')
    a = 'Você deve se alistar urgentemente, já passou {} anos do esperado'.format(idade - 18)
elif 21 >= idade > 18:
    if idade == 19:
        b = 'só se passou'
    else:
        b = 'se passaram'
    print('Você deveria ter se alistado')
    a = f'Ainda dá tempo, {b} {idade - 18} do esperado'
else:
    a = 'Você pode se alistar agora mesmo'
print(f'{a}')
# ano
from datetime import date
data = date.today().year
ano = int(input('Em que ano você nasceu? '))
calc = data - ano
print(f'no ano atual({data}) você têm {calc} anos')
if calc < 18:
    print(f'''Você ainda vai se alistar
Faltam {18 - calc} anos ({data + (18 - calc)})''')
elif calc > 21:
    print(f'''Já passou da hora!!
Já se passaram {calc - 18} anos do esperado ({ano + 18})''')
elif 21 >= calc > 18:
    if calc == 19:
        frase = 'Ainda dá tempo\nSó se passou 1 ano'
    else:
        frase = f'Você está atrasado!\nSe passaram {calc - 18} anos'
    print(f'{frase} do esperado ({ano + 18})')
else:
    print('Você pode se alistar agora mesmo')
