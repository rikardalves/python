a = float(input('First length (cm): '))
b = float(input('Second length (cm): '))
c = float(input('Third length (cm): '))
if a < b + c and b < a + c and c < a + b:
    print('Can form a triangle')
else:
    print("Can't form a triangle")
