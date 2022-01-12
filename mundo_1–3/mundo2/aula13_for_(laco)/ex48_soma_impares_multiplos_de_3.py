a, b = 0, 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        a += c
        b += 1
print(f'A soma dos ímpares múltiplos de 3 é {a} e a quantidade de números é {b}')
