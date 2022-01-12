def readmoney(content):
    valid = False
    while not valid:
        inp = str(input(content)).replace(',', '.').strip()
        if inp.isalpha() or inp == '':
            print(f'\033[31mO valor "{inp}" é inválido\033[m')
        else:
            return float(inp)


def readint(msg):
    while True:
        num = str(input(msg))
        if num.isdecimal():
            num = int(num)
            break
        else:
            print('\033[1;31mErro, digite um número inteiro\033[m')
    return num
