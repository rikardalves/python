from lib.verifications import *


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
        
        
        namefile = f'{str(self.holder.name)}{str(self.holder.surname)}.txt'
        enter = have_create(namefile)
        if not enter:
            writedoc(
                namefile, 
                f'CADASTRO NA DATA {self.create}\n'
                f'Número da conta: {self.accnum}\n'
                f'Nome do titular: {self.holder.name}\n'
                f'Sobrenome do titular: {self.holder.surname}\n'
                f'CPF do titular: {self.holder.cpf}\n'
                f'SALDO: {self.balance}\n'
                f'LIMITE: {self.limit}\n{"—" * 50}\n'
                )
    
    
    def deposit(self, value):
        value = rfloat(value)
        if not value:
            return False
        else:
            self.balance += value
            namefile = f'{str(self.holder.name)}{str(self.holder.surname)}.txt'
            save = f'Depósito: R${value:.2f} | {self.historic.ctime}\n'
            writedoc(namefile, save)
            self.historic.transfers.append(save)
            return True
    
    
    def withdraw(self, value):
        value = rfloat(value)
        if not value:
            return False
        elif value > self.balance:
            namefile = f'{str(self.holder.name)}{str(self.holder.surname)}.txt'
            save = f'Tentativa de saque: R${value:.2f}'
            save += f' | {self.historic.ctime}\n'
            writedoc(namefile, save)
            self.historic.transfers.append(save)
            return False
        else:
            self.balance -= value
            namefile = f'{str(self.holder.name)}{str(self.holder.surname)}.txt'
            save = f'Saque: R${value:.2f} | {self.historic.ctime}\n'
            writedoc(namefile, save)
            self.historic.transfers.append(save)
            return True
    
    
    def transfer_to(self, person, value):
        value = rfloat(value)
        if not value:
            return False
        elif value > self.balance:
            namefile = f'{str(self.holder.name)}{str(self.holder.surname)}.txt'
            save = f'Tentativa de transferência de '
            save += f'R${value:.2f} para CVC/CVV '
            save += f'{person.accnum} | {self.historic.ctime}\n'
            writedoc(namefile, save)
            self.historic.transfers.append(save)
            return False
        else:
            self.balance -= value
            person.balance += value
            namefile = f'{str(self.holder.name)}{str(self.holder.surname)}.txt'
            depfile = f'{str(person.holder.name)}{str(person.holder.surname)}.txt'
            save = f'Transferência de R${value:.2f} '
            save += f'para CVC/CVV {person.accnum}'
            save += f'| {self.historic.ctime}\n'
            writedoc(namefile, save)
            self.historic.transfers.append(save)
            
            writedoc(depfile, f'Depósito de CVC/CVV {self.accnum}:'
                f'R${value:.2f} | {self.historic.ctime}\n')
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
                print(f'\033[7;36m{content.strip()}\033[m')
            else:
                print(f'\033[7m{content.strip()}\033[m')
        print('—' * maxlen)
