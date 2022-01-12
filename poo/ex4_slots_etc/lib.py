class Conta:
    
    __slots__ = ['_number', '_holder', '_balance', '_limit', '_ident']
    ident = 1
    
    def __init__(self, number, holder, balance, limit=1000):
        self._number = number
        self._holder = holder
        self._balance = balance
        self._limit = limit
        self._ident = Conta.ident
        Conta.ident += 1
    
    
    @property
    def _Conta__balance(self):
        return self._balance
    
    
    @_Conta__balance.setter
    def _Conta__balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            self._balance = 0
            print('NOPPERS! Sem negatividade')
