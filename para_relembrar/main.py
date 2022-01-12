from lib.classes import *
from lib.batalha import *
from random import shuffle, randint

# Variáveis do player
player = apply_class(input('Nome do personagem: '))
player_position = None
player.dodge_direc = positions()

# Variáveis do bot
bot = Bot('Callen')
bot_position = None

# Ordem de início
members = [bot, player]
shuffle(members)

auto_attack = int(input('Quer ativar o auto ataque?\n[1] Sim\n[2] Não\n'))
while bot.life > 0 and player.life > 0:
    for turn in range(0, 2):
        # Ações do bot
        if type(members[turn]) == Bot:
            bot_position = bot.dodge()
            bot.dodge_direc = bot_position
            atk_bot_direc = randint(0, 1)
            bot.attack(player, atk_bot_direc)
            print(f'Status do {bot.name}')
            print(f'Posição: {bot.dodge_direc}')
            print(f'Vida: {bot.life}')
        # acões do player
        else:
            print('Seus status atuais')
            print(f'Posição: {player.show_position(player.dodge_direc)}')
            print(f'Vida: {player.show_life()}')
            attack_move = int(input('Deseja se mover?\n[1] Sim\n[2] Não\n'))
            if attack_move == 1:
                player_position = input_position()
                player.dodge_direc = player_position
                if type(player_position) is int:  # Validação de mudança de posição
                    player_place = positions(player_position)
                confirm = 1
                if auto_attack == 2:
                    confirm = int(input('Deseja atacar?\n[1] Sim\n[2] Não\n'))
                # Atacar em x direção
                if confirm == 1:
                    print('Deseja atacar em que direção?\n[1] À esquerda\n[2] À direita')
                    atk_direction = int(input()) - 1
                    player.attack(bot, atk_direction, show=True)
            else:
                print('Ok')
if bot.life <= 0:
    print('\033[32mParabéns! Você ganhou esta luta')
elif player.life <= 0:
    print('\033[31mMais sorte da próxima vez. Você perdeu a luta')
