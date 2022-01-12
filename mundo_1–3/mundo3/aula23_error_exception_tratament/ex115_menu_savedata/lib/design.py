def line(larger=48):
    return '─' * larger


def header(msg, tcolor='', larger=48):
    print(line(larger))
    print(f'\033[{tcolor}m{str(msg).center(larger)}\033[m')
    print(line(larger))


def menu(clist, headerr=False, mark=False, mcolor='', ccolor='', extens=48):
    if not headerr:
        print(line(extens))
    if mark:
        for cont, element in enumerate(clist):
            print(f'\033[{mcolor}m{cont + 1}\033[m-\033[{ccolor}m{element}\033[m', end='')
    else:
        for element in clist:
            print(f'\033[{ccolor}m{element}\033[m', end='')
    print(line(extens))


def menuu(title, clist=None, color=False, mark=False):
    # Validando title como str
    try:
        len(title)
    except:
        return print('Os parâmetro devem ser respectivamente: string e lista')
    else:
        qntitle = len(title)

    # Catalogando a quantidade de palavras da frase mais extensa
    bigger = qntitle
    if clist is not None:
        for phrase in clist:
            if bigger < len(phrase):
                bigger = len(phrase)
    bigger += 12

    # Montagem do menu
    print('─' * bigger)
    print(f"{title.center(bigger)}")
    print(f"{'─' * bigger}")
    if clist is not None:
        if not color:
            yellow = '\033[m'
            blue = '\033[m'
        else:
            yellow = '\033[33m'
            blue = '\033[34m'
        cont = 0
        if mark:
            for cont, element in enumerate(clist):
                print(f'{yellow}{cont + 1}\033[m-{blue}{element}\033[m', end='')
        else:
            for element in clist:
                print(f'{blue}{element}\033[m', end='')
        print('─' * bigger)
        return cont + 1


def readint(msg):
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário optou por não digitar um valor\033[m')
            return 0
        else:
            return num


def qnttint(limit, msg):
    try:
        limit = int(limit)
    except:
        return print('O parâmetro limit deve ser inteiro')
    while True:
        try:
            value = int(input(msg))
            if value > limit or value < 1:
                print('\033[31mNão há esta opção para celeção\033[m')
                continue
        except (ValueError, TypeError):
            print('\033[31mDigite um valor válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mSem valor de entrada. Valor atribuido: 0\033[m')
            return 0
        else:
            return value
