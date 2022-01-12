# 2m²/L
h = float(input('Height: '))
w = float(input('Width: '))
hw = h * w
print('Area: {}m²\nLiters of paint needed: {}L'.format(hw, hw / 2))
# Xm²/L
r = float(input('Ink yield(m²/L): '))
print('Liters of paint needed: {:.2f}L'.format(hw / r))
