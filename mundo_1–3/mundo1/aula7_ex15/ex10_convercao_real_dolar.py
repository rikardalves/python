v = float(input('Insert the value: R$'))
print('The value in dollar is US${:.2f}'.format(v / 5.05))
# Com a fómula simplificada do format
print(f'The value in dollar is US${v / 5.05}')
