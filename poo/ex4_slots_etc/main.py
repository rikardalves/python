from lib import *


acc = Conta('123-4', 'Alberto', -6)
print(acc._balance)
acc._balance = 50
print(acc._balance)
print(acc.ident)
acc2 = Conta('', '', 8)
print(acc2.ident)
print(acc.ident)
