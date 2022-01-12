s = float(input('Wage: R$'))
c = int(input('Percentage: '))
print('The increase will be R${:.2f}'.format(s + (c/100 * s)))
