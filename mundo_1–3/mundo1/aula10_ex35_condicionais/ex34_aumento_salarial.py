sa = float(input('Type you salary: R$ '))
if sa > 1250:
    print('You salary will increase from R${:.2f} to R${:.2f}'.format(sa, sa + (sa * 0.1)))
else:
    print('Your salary will increase from R${:.2f} to R${:.2f}'.format(sa, sa + (sa * 0.15)))
