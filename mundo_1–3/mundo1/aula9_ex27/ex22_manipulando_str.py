Nome = input('What is your name? ')
M = Nome.upper()
m = Nome.lower()
p = Nome.split()
c = len(''.join(p))
print('''Uppercase: {}\nLowercase: {}\nHow many letters: {}
How many letters(first name): {}'''.format(M, m, c, len(p[0])))
# Método do professor
Nome = input('What is your name: ').strip()
print('''Uppercase: {}\nLowercase: {}\nHow many letters: {}
How many letters(First name): {}'''.format(M, m, len(Nome) - Nome.count(' '),
                                           Nome.find(' ')))
