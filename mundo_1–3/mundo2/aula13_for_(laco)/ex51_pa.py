termo = float(input('Primeiro termo da PA: '))
razao = float(input('Razão da PA: '))
for c in range(0, 9):
    if termo % 1 != 0:
        print('{:.1f}'.format(termo), end=', ')
    else:
        print(int(termo), end=', ')
    termo += razao
print('{:.1f}'.format(termo)) if termo % 1 != 0 else print(int(termo))

# Método do professor

term, raza = int(input('Primeiro termo: ')), int(input('Razão: '))
decimo = term + 9 * raza
z = ''
for c in range(term, decimo, raza):
    z += str(c) + ', '
print(z[:len(z) -2])

# Outra forma linha 3:9

# z = ''
# for c in range(0, 10):
#     if termo % 1 != 0:
#         a = str(termo % 1)
#         z += str(int(termo)) + '.' + a[2] + ', 'qq
#     else:
#         z += str(int(termo)) + ', '
#     termo += razao
# print(z[:len(z) - 2])
