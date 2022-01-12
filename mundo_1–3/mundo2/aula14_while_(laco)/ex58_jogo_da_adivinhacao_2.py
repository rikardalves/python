from random import randint
from time import sleep
num = 4
acum = ''
for c in range(1, 37):
    cor = '\033[1;3' + str(num) + 'm'
    acum = cor + '*' + acum
    if num == 4:
        num += 2
    elif num < 7:
        num += 1
    elif num == 7:
        num = 4
cp = randint(1,100)
print(acum + '\n*\033[1;00m BEM VINDO AO JOGO DA ADIVINHAÇÃO\033[1;34m *\n' + acum)
tent = 5
p1 = 0
print('\033[1;32mVocê tem 5 tentativas, boa sorte :)')
while p1 != cp and tent != 0:
    if tent == 5:
        p1 = int(input('\033[mDigite um número entre 1 e 100: ')) 
    else:
        p1 = int(input('\033[mTente novamente: ')) 
    if p1 == cp:
        print('Você acertou')
    elif p1 > cp and tent != 1:
        if p1 - cp <= 5:
            print('Está próximo, mas é menor que isso')
        else:
            print('É menor que isso')
    elif p1 < cp and tent != 1:
        if p1 - cp <= 5:
            print('Está próximo, mas é maior que isso')
        else:
            print('É maior que isso')
    tent -= 1
    m = s = ''
    if tent != 1:
        m, s = 'm', 's'
    if tent != 0 and p1 != cp:
        print(f'Resta{m} {tent} tentativa{s}')
if tent == 0:
    print(f'Suas tentativas acabaram, escolhi o número {cp}')
