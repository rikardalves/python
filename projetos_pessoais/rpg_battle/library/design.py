def line(length=44):
    return '-' * length


def between_bars(content="", color=""):
    from math import ceil
    from math import floor
    # Tamanho padrão: 44 espaços

    # Discontar x espaços
    try:
        discount = len(content) / 2
    except:
        discount = 0
    return f'|{color}{" " * (22 - floor(discount))}{content}{" " * (22 - ceil(discount))}\033[m|'
