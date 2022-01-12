def rfloat(value):
    try:
        value = float(value)
    except:
        try:
            if ',' in str(value) or ' ' in str(value):
                value = float(value.replace(',', '.'))
        except:
            value = False
    return value
    


class Client:
    def __init__(self, name, surname, cpf):
        # Validação
        name = str(name).strip().title()
        if name == '':
            name = False
        
        surname = str(surname).strip().title()
        if surname == '':
            surname = False
        
        cpf = str(cpf).replace('-', '').replace('.', '')
        if not len(cpf) == 11 or not cpf.isnumeric():
            cpf = False
        else:
            cpf = list(cpf)
            cpf = str(f"{''.join(cpf[:3])}.{''.join(cpf[3:6])}"
            f".{''.join(cpf[6:-2])}-{''.join(cpf[-2:])}")
        
        # Atributos universais
        self.name = name
        self.surname = surname
        self.cpf = cpf


class Account:
    def __init__(self, client, balance, limit=1000):
        # Validação
        from random import randint
        
        
        accnum = ''
        for cont in range(0, 3):
            random = randint(1, 9)
            accnum += str(random)
        
        if type(client) != Client:
            client = False
        
        balance = rfloat(balance)
        
        limit = rfloat(limit)
        
        # Atributos universais
        self.accnum = int(accnum)
        self.holder = client
        self.balance = balance
        self.limit = limit
        self.historic = Historic()
        self.create = self.historic.ctime
    
    
    def deposit(self, value):
        value = rfloat(value)
        if not value:
            return False
        else:
            self.balance += value
            self.historic.transfers.append(
                f'Depósito: R${value:.2f} | {self.historic.ctime}'
                )
            return True
    
    
    def withdraw(self, value):
        value = rfloat(value)
        if not value:
            return False
        elif value > self.balance:
            self.historic.transfers.append(
                f'Tentativa de saque: R${value:.2f}'
                f' | {self.historic.ctime}'
                )
            return False
        else:
            self.balance -= value
            self.historic.transfers.append(
                    f'Saque: R${value:.2f} | {self.historic.ctime}'
                    )
            return True
    
    
    def transfer_to(self, person, value):
        value = rfloat(value)
        if not value:
            return False
        elif value > self.balance:
            self.historic.transfers.append(
                f'Tentativa de transferência de '
                f'R${value:.2f} para CVC/CVV '
                f'{person.accnum} | {self.historic.ctime}'
                )
            return False
        else:
            self.balance -= value
            person.balance += value
            self.historic.transfers.append(
                f'Transferência de R${value:.2f} '
                f'para CVC/CVV {person.accnum}'
                f'| {self.historic.ctime}'
                )
            return True
    
    
    def extract(self):
        print(f'Titular(nome): {self.holder.name}')
        print(f'CVC/CVV: {self.accnum}')
        print(f'Saldo: {self.balance}')


class Historic:
    def __init__(self):
        from datetime import datetime
        self.ctime = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
        self.transfers = []
    
    
    def printh(self):
        for count, line in enumerate(self.transfers):
            if count == 0:
                maxlen = len(line)
            elif len(line) > maxlen:
                maxlen = len(line)
        print('—' * maxlen)
        
        for cont, content in enumerate(self.transfers):
            if cont % 2 == 0:
                print(f'\033[7;36m{content}\033[m')
            else:
                print(f'\033[7m{content}\033[m')
        print('—' * maxlen)
