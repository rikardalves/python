from colorama import *
init(autoreset=True)
cy = Fore.LIGHTCYAN_EX
valor = float(input(cy + 'Qual o valor da casa que será financiada? R$'))
sa = float(input(cy + 'Qual o seu salário? R$'))
tempo = int(input(cy + 'Em quantos anos pretende financiar? '))
div = valor / (tempo * 12)
if div > 0.3 * sa:
    print(Fore.LIGHTRED_EX + 'Você não poderá financiar esta casa, pois o gasto mensal seria de {:.2f}% do seu salário.'
          ''.format((100 * div) / sa))
    f1, f2 = 'tería', 'excedendo 30% do salário'
else:
    print(Fore.LIGHTGREEN_EX + 'Você poderá financiar este imóvel, gastando mensalmente {:.2f}% '
          'do seu salário.'.format((100 * div) / sa))
    f1, f2 = 'terá', 'ficando abaixo de 30% do salário'
print(Fore.LIGHTWHITE_EX + 'Você {} o gasto de R${:.2f}, {}'.format(f1, div, f2))
