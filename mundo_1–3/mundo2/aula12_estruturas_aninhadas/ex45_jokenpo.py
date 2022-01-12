from random import choice, randint
from time import sleep
esc = int(input('Por extenso (1) ou seleção por número(2)? '))
lista = ['pedra', 'papel', 'tesoura']
ran = str(choice(lista))
# Segunda randomização
to = ('pedra', 'papel', 'tesoura')
ra = randint(0, 2)
if esc == 1:
    ch = str(input('Vamos jogar pedra, papel, tesoura? escolha e digite um deles aqui: ')).strip().lower()
    if 'tesoura' in ch or 'papel' in ch or 'pedra' in ch:
        print('Jo')
        sleep(0.5)
        print('Ken')
        sleep(0.5)
        print('PÔ!')
        print(f'eu escolhi {ran}!', end=' ')
    if 'pedra' in ch and 'pedra' in ran or 'tesoura' in ch and 'tesoura' in ran or 'papel' in ch and 'papel' in ran:
        print('Empatamos')
    elif 'tesoura' in ch and 'papel' in ran or 'papel' in ch and 'pedra' in ran or 'pedra' in ch and 'tesoura' in ran:
        print('Você ganhou')
    elif 'tesoura' in ran and 'papel' in ch or 'papel' in ran and 'pedra' in ch or 'pedra' in ran and 'tesoura' in ch:
        print('Você perdeu')
    else:
        print('Digite uma das opções corretamente')
# Quebra de método 1
elif esc == 2:
    print('''Vamos jogar pedra, papel, tesoura?
[1] Pedra
[2] Papel
[3] Tesoura''')
    ch = int(input(''))
    if ch == 1 or ch == 2 or ch == 3:
        print('Jo'), sleep(0.5), print('Ken'), sleep(0.5), print('PÔ!')
    if ra == 0 and ch == 1 or ra == 1 and ch == 2 or ra == 2 and ch == 3:
        print(f'Eu escolhi {to[ra]}! Empatamos!')
    elif ra == 0 and ch == 2 or ra == 1 and ch == 3 or ra == 2 and ch == 1:
        print(f'Eu escolhi {to[ra]}! Você ganhou')
    elif ra == 0 and ch == 3 or ra == 1 and ch == 1 or ra == 2 and ch == 2:
        print(f'eu escolhi {to[ra]}! Você perdeu')
    else:
        print('Digite um valor válido')
