p = float(input('Price: R$'))
c = int(input('Percentage: '))
print('The value R${:.2f} with the discount of {}% results in the value of R${:.2f}'.format(p, c, p - p * (c/100)))
