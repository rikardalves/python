D = int(input('Days with the vehicle(R$60.00/day): '))
km = float(input('kilometers traveled(R$0.15/day): '))
print('The amount to be paid will be R${:.2f}'.format(60 * D + 0.15 * km))
