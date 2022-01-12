def create_acc(number, holder, balance, limit):
    acc = {'number':number, 'holder':holder, 
    'balance':balance, 'limit':limit}
    return acc


def deposit(acc, value):
    acc['balance'] += value
    return acc


def withdraw(acc, value):
    acc['balance'] -= value
    return acc


def extract(acc):
    print(f'Número: {acc["number"]}')
    print(f'Saldo: {acc["balance"]}')
