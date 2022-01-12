v = int(input('Digite o número que quer saber a tabuada: '))
for c in range(0,11):
    if c ==0 or c==3 or c==6 or c==9:
        print('| ', end='')
    print(f'{c} x {v} = {v * c}', end=' | ')
    if c == 2 or c == 5 or c == 8:
        print('\n')