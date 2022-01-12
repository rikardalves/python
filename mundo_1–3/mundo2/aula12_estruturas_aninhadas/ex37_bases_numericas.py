from colorama import *
num = str(input('Digite um número inteiro e se que convertê-lo para binário, octal ou hexadecimal: ').strip().lower())
n = num.split()
init(autoreset=True)
branco = Fore.LIGHTWHITE_EX
if 'bin' in num:
    print(branco + 'O número {} em binário é {}'.format(n[0], Fore.LIGHTGREEN_EX + bin(int(n[0]))[2:]))
elif 'oct' in num:
    print(branco + 'O número {} em octal é {}'.format(n[0], Fore.LIGHTYELLOW_EX + oct(int(n[0]))[2:]))
elif 'hex' in num or 'ex' in num:
    print(branco + 'O número {} em hexadecimal é {}'.format(n[0], Fore.LIGHTMAGENTA_EX + hex(int(n[0]))[2:]))
else:
    print(Fore.LIGHTRED_EX + 'Por favor, digite uma base numérica válida')
