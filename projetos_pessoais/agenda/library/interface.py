from library.analisys import *

def c(content, color, bold=False):
    if bold:
        bold = '1;'
    else:
        bold = ''
    # Validação de color e definição de cores
    color = str(color).strip().lower()
    if color == 'r':
        color = '\033[' + bold + '31m'
    elif color == 'g':
        color = '\033[' + bold + '32m'
    elif color == 'y':
        color = '\033[' + bold + '33m'
    elif color == 'b':
        color = '\033[' + bold + '34m'
    elif color == 'l':
        color = '\033[' + bold + '35m'
    elif color == 'c':
        color = '\033[' + bold + '36m'
    elif color == 'n':
        color = '\033[' + bold + 'm'
    reset = '\033[m'
    msg = f'{color}{content}{reset}'
    return msg


def line(larger=50):
    paramvalid = rint(larger)
    if paramvalid == 0:
        larger == 50
    print('—' * larger)


def header(txt, larger=50):
    txt = str(txt).strip()
    line(larger)
    print(txt.center(larger))
    line(larger)


def body(content, mark=True, colorc='n', larger=50):
    rlist(content)
    rint(larger)
    for cont, option in enumerate(content):
        option = option.replace('\n', '')
        if not mark:
            print(c(option, colorc))
        else:
            if mark:
                mark = 'n'
            print(
                f'{c(cont + 1, mark)} '
                f'— {c(option, colorc)}'
                )
