from library import battle
from library import classes
from library import design
from library import field

# Start -->
# Nome de usuário
name = str(input('Digite seu nome de usuário: '))
# Configurações
auto_attack_state = False
show_aa_state = ('Sim', 'Não')
selected_aa_state = 2

difficulty = ('Easy', 'Normal', 'Hard')
selected_difficulty = 1

# Menu
# Design
print(' ', end='')
print(design.line())

print(design.between_bars('MENU', '\033[1;33m'))
print('|', end='')
print(design.line(), end='')
print('|')
print(design.between_bars('1 - Jogar', '\033[1m'))
print(design.between_bars('2 - Opções', '\033[1m'))
print(design.between_bars('3 - Sair', '\033[1m'))

print(' ', end='')
print(design.line())

# Aplicação
while True:
    menu_error_message = 'Por favor escolha uma opção entre as três possíveis'

    # Configurações na tela
    if not auto_attack_state:
        show_aa_state = 'Não'
    elif auto_attack_state:
        show_aa_state = 'Sim'

    try:
        # Escolha de cada opção do menu
        menu_choice = int(input(f'{" " * 17}Selecionar: '))

        if menu_choice == 1:
            pass
        elif menu_choice == 2:

            print(' ', end='')
            print(design.line())

            print(design.between_bars('CONFIGURAÇÕES', '\033[1;34m'))
            print('|', end='')
            print(design.line(), end='')
            print('|')
            print(design.between_bars(f'Auto-ataque: {show_aa_state}'))
            print(design.between_bars(f'Dificuldade: {difficulty[selected_difficulty]}'))

            print(' ', end='')
            print(design.line())

            # Seleção de opção na configuração
            config_choice = int(input(f'{" " * 17}Selecionar: '))
        elif menu_choice == 3:
            exit()
        else:
            print(menu_error_message)

    except KeyboardInterrupt:
        print('\nDeseja sair do jogo? \n[1] Sim\n[2] Não')
        exit_ask_menu = int(input())
        if exit_ask_menu == 1:
            exit()
        else:
            continue

    except:
        design.line(51)
        print(menu_error_message)
        design.line(51)
        continue
