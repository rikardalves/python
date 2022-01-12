from lib import *


client1 = client(
    input('Nome: '), input('Sobrenome: '), input('CPF: ')
    )
account1 = account(client1, 0)
print(account1._number)
account2 = account(37, 0)
print(account2._number)
account2._number = 6
print(account.number)
print(vars(account))
