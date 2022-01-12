n1 = int(input('Type a value: '))
n2 = int(input('Type a value: '))
r = n1 + n2
print('The sum is', r)
print('The sum between {}{}{} and {}{}{} is {}{}'
      ''.format('\033[35m', n1, '\033[m', '\033[35m', n2, '\033[m', '\033[36m', r))
