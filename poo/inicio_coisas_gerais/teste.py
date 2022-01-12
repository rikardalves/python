choice = int(input())

if choice == 1:
    class Conta:
        pass
    
    
    # Para cada nova instância deve-se colocar os atributos que queremos
    conta = Conta()
    conta.titular = 'Ríkard'
    conta.saldo = 3000
    conta.numero = '111-1'
    print(conta.saldo)
    #A saída será 3000
    
    # Exemplo de erro
    '''
    conta1 = Conta()
    print(conta1.saldo)
    '''
    # Neste exemplo o atributo saldo não está linkado à instância


elif choice == 2:
    class Conta:
        def __init__(self, titular, saldo, numero):
            self.titular = titular
            self.saldo = saldo
            self.numero = numero
    
    
    # Agora devemos especificar os parâmetros obrigatórios ao instanciar um objeto
    conta = Conta('Ríkard', 3000, '111-1')
    conta2 = Conta('jdjd', 3, '373-2')
    print(conta2.saldo, conta.saldo)
    
    # Caso façamos isso dará TypeError
    '''conta = Conta()
    conta.saldo = 3000
    print(conta.saldo)'''


elif choice == 3:
    class Conta:
        def __init__(self, titular, saldo, numero):
            self.titular = titular
            self.saldo = saldo
            self.numero = numero
        
        
        # Adicionando mais uma funcionalidade(método) à instância
        def depositar(self, valor):
            self.saldo += float(valor)
    
    
    conta = Conta('Ríkard', 3000, '111-1')
    print(conta.saldo)
    # Na vida real seria "Deposite na minha conta", nos códigos só inverte um pouco as coisas
    conta.depositar(3000)
    print(conta.saldo)


elif choice == 4:
    # Código final
    class Conta:
        def __init__(self, titular, saldo, numero):
            self.titular = titular
            self.saldo = saldo
            self.numero = numero
        
        
        def depositar(self, valor):
            self.saldo += float(valor)
        
        
        def sacar(self, valor):
            self.saldo -= float(valor)
        
        
        def extrato(self):
            print(f'Conta: {self.numero}')
            print(f'Saldo: {self.saldo}')
    
    
    conta = Conta('Ríkard', 3000, '111-1')
    conta.extrato()
    conta.depositar(3000)
    conta.extrato()
    conta.sacar(20)
    conta.extrato()

elif choice == 5:
    # Código final com return
    class Conta:
        def __init__(self, titular, saldo, numero):
            self.titular = titular
            self.saldo = saldo
            self.numero = numero
        
        
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
    
    
    conta = Conta('Ríkard', 3000, '111-1')
    conta.extrato()
    conta.depositar(3000)
    conta.extrato()
    saque = conta.sacar(1001000)
    if saque:
        print('Êxito no saque')
    else:
        print('Saque um valor abaixo do seu saldo')
    conta.extrato()


elif choice == 6:
    # Código final 2
    class Conta:
        def __init__(self, titular, saldo, numero):
            self.titular = titular
            self.saldo = saldo
            self.numero = numero
        
        
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
    
    
    conta = Conta('Ríkard', 3000, '111-1')
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
