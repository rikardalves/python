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


def readfloat(msg):
    value = 0
    while True:
        try:
            value = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mO valor {value} é inválido\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário optou por não digitar um valor\033[m')
            return 0
        else:
            return value
