t1 = float(input('1º termo da PA: '))
r = float(input('Razão: '))
q = int(input('Quantidade de termos: '))
while q > 0:
    if t1 % 1 != 0:
        a = f'{t1:.1f}'
    else:
        a = int(t1)
    print(str(a).replace('.', ','), end='')
    print(', ' if q != 1 else "", end='')
    t1 += r
    q -= 1

# print('\n%.1f' % 1.234)

t = float(input('\n1º termo da PA: '))
raz = float(input('Razão: '))
quant = int(input('Quantidade de termos: '))
for c in range(1, quant + 1):
    if t % 1 != 0:
        b = f'{t:.1f}'
    else:
        b = int(t)
    print(str(b).replace('.', ','), end='')
    print(', ' if c != quant else '', end='')
    t += raz
