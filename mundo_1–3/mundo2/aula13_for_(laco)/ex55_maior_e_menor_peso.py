M = 0
m = 0
for c in range(1, 6):
    peso = float(input(f'{c}º peso: '))
    if peso > M:
        M = peso
    if c == 1:
        m = peso
    else:
        if peso < m:
            m = peso
print(f'O maior peso é {M}, e o menor peso é {m}')