from func import *

account = create_acc('131-4', 'Ríkard', 3872.20, 2000)
extract(account)
account = deposit(account, 200)
extract(account)
account = withdraw(account, 45.20)
extract(account)
