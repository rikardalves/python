from random import shuffle
n1 = input('Name 1: ')
n2 = input('Name 2: ')
n3 = input('Name 3: ')
n4 = input('Name 4: ')
L = [n1, n2, n3, n4]
shuffle(L)
print('{}'.format(L))
