N = str(input('Type you name: ')).strip().title()
S = N.split()
print('Your first name is {}\nYour last name is {}'.format(S[0], N[N.rfind(' '):]))
# Método do professor
print('Your first name is {}\nYour last name is {}'.format(S[0], S[len(S) - 1]))
