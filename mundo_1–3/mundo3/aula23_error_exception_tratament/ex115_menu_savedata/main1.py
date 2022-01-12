from lib.design import *
from lib.records import *
from colorama import Fore
from time import sleep

file = 'database.txt'

if not filexists(file):
    addfile(file)

while True:
    header('MENU PRINCIPAL')
    menu(
        ['Ver pessoas cadastradas\n', 'Cadastrar novas pessoas\n', 'Sair do sistema\n'], True, True, 33, 34
    )
    option = readint(Fore.LIGHTGREEN_EX + 'Sua opção: \033[m')
    if option == 1:
        readfile(file)
    elif option == 2:
        header(f'NOVO CADASTRO')
        while True:
            nome = readname('Nome: ')
            if not surname(nome):
                print('\033[31mNome completo por favor\033[m')
            elif repet(file, nome):
                print('\033[31mNome já existente nos registros\033[m')
            else:
                break
        idade = readint('Idade: ')
        saveinfo(file, nome, idade)
    elif option == 3:
        menu('Saindo do sistema...\n')
        sleep(0.8)
        print('Até mais!')
        break
    else:
        print('\033[31mDigite um valor válido\033[m')
