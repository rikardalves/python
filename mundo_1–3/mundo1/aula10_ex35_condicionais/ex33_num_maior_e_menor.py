n1 = int(input('first number: '))
n2 = int(input('Second number: '))
n3 = int(input('Third number: '))
M = n1
if n2 > n1 and n2 > n3:
    M = n2
if n3 > n1 and n3 > n2:
    M = n3
m = n1
if n2 < n1 and n2 < n3:
    m = n2
if n3 < n1 and n3 < n2:
    m = n3
print(f'The {M} is the highest number')
print(f'The {m} is the smallest number')
