from lib.design import *
from lib.records import *
from colorama import Fore
from time import sleep

file = 'database.txt'

if not filexists(file):
    addfile(file)

while True:
    menuu(
        'SISTEMA', ['Ver cadastradas\n', 'Cadastrar novas pessoas\n', 'Sair do sistema\n'], True, True
    )
    option = readint(Fore.LIGHTYELLOW_EX + 'Sua opção: \033[m')
    if option == 1:
        menuu(f'PESSOAS CADASTRADAS', readfile(file))
    elif option == 2:
        menuu(f'NOVO CADASTRO')
        nome = input('Nome: ').strip().title()
        idade = readint('Idade: ')
        saveinfo(file, nome, idade)
    elif option == 3:
        menuu('Saindo do sistema...')
        sleep(0.8)
        print('Até mais!')
        break
    else:
        print('\033[31mDigite um valor válido\033[m')
