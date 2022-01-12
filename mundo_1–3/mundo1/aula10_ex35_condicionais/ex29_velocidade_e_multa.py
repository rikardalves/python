vel = float(input('What was the maximum speed reached? '))
if vel > 80.0:
    print('The maximum speed acceptable is 80km/h')
    print('You were fined, your traffic ticket is R${:.2f}'.format((vel - 80) * 7))
else:
    print("""You were withing the speed limit
Everything is alright!""")
