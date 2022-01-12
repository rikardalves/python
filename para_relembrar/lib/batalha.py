def positions(choice=None):
    position = [0, 0]
    try:
        if choice not in (0, 1):
            return position
        else:
            position[choice] = 1
            return position
    except:
        return position


def input_position():
    try:
        move_to = int(input('[1] Esquivar para a esquerda\n[2] Esquivar para a direita\n')) - 1
        return move_to
    except KeyboardInterrupt:
        keyboardinterrupt()
    except ValueError:
        return None


def tprint(content, end='\n'):
    from time import sleep

    content = str(content)
    for element in content:
        if element != content[-1]:
            print(element, end='', flush=True)
            sleep(0.2)
        else:
            print(element, end=end)


def keyboardinterrupt():
    while True:
        try:
            answer = int(input('\nQuer realmente parar? \n[1] Sim\n[2]Não\n'))
            if answer == 1:
                exit()
            elif answer == 2:
                break
        except (ValueError, KeyboardInterrupt):
            continue


def line(length=53):
    return '─' * length


def center(content, length=53):
    return f'\033[1m{content}\033[m'.center(length)
