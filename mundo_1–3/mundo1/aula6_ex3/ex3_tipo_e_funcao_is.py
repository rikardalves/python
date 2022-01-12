from colorama import *
o = input('Type something: ')
init(autoreset=True)
w = Fore.LIGHTWHITE_EX + '\033[7;1m'
print(type(o))
print('{}"{}" is a space?\033[0;40m {}{} '.format(w, o, Fore.LIGHTRED_EX + Back.BLACK, o.isspace()))
print('"{}" is a alphanumeric?'.format(o), o.isalnum())
print('"{}" is alphabetic?'.format(o), o.isalpha())
