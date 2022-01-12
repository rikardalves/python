choice = int(input())

if choice == 1:
    # Código final 2 param opcional
    class Conta:
        def __init__(self, titular, saldo, numero, limite = 1000):
            self.titular = titular
            self.saldo = saldo
            self.numero = numero
            self.limite = limite
        
        
        def depositar(self, valor):
            self.saldo += float(valor)
        
        
        def sacar(self, valor):
            if self.saldo < valor:
                return False
            else:
                self.saldo -= float(valor)
                return True
        
        
        def transferir(self, destino, valor):
            retirada = self.sacar(valor)
            if retirada:
                destino.depositar(valor)
                return True
            else:
                return False
        
        
        def extrato(self):
            print(f'Conta: {self.numero}')
            print(f'Saldo: {self.saldo}')
    
    
    conta = Conta('Ríkard', 3000, '111-1', 2000)
    conta2 = Conta('Desconhecido', 0, '222-2')
    print(conta2.saldo, conta.saldo)
    conta.extrato()
    conta.depositar(3000)
    conta.extrato()
    saque = conta.sacar(1001000)
    if saque:
        print('Êxito no saque')
    else:
        print('Saque um valor abaixo do seu saldo')
    conta.extrato()
    conta.transferir(conta2, 2500)
    print(conta2.saldo, conta.saldo)
    conta2.extrato()


elif choice == 2:
    # Código final com return
    class Conta:
        def __init__(self, titular, saldo, numero, limite = 1000):
            self.titular = titular
            self.saldo = saldo
            self.numero = numero
            self.limite = limite
        
        
        def depositar(self, valor):
            self.saldo += float(valor)
        
        
        def sacar(self, valor):
            if self.saldo < valor:
                return False
            else:
                self.saldo -= float(valor)
                return True
        
        
        def extrato(self):
            print(f'Conta: {self.numero}')
            print(f'Saldo: {self.saldo}')
    
    
    conta = Conta('Ríkard', 3000, '111-1', 2000)
    conta.extrato()
    conta.depositar(3000)
    conta.extrato()
    saque = conta.sacar(1001000)
    if saque:
        print('Êxito no saque')
    else:
        print('Saque um valor abaixo do seu saldo')
    conta.extrato()
