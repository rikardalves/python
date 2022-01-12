acum = 0
name = ''
o = 0
cont = 0
cor = ''
for c in range(1, 5):
    n = input(f'Nome da {c}ª pessoa: ' ).strip().title()
    d = n.split()
    i = int(input(f"Idade de {d[0]}: "))
    s = input(f'Sexo de {d[0]} (M, F ou T): ').lower()
    acum += i
    if 'm' in s and i > o:
        name = n
        o = i
    if 'f' in s and i < 20:
        cont += 1
    if 'm' not in s and 'f' not in s and 't' not in s or len(s.split()) != 1:
        print('\n\033[1;31mAVISO: esta pessoa será desconsiderada\033[m')
    if c == 4:
        cor = '\033[1;32m'
    print(f'{cor}' + '_' * (23 + len(d[0] + s)), '\033[m\n')
print(f'''Média de idade: {(acum/c):.0f}
Pessoa do sexo masculino mais velha: {name}
Pessoas do sexo feminino com menos de 20 anos: {cont}''')
