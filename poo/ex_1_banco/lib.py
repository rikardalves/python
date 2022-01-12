class client:
    
    __slots__ = ['_name', '_surname', '_cpf']
    
    def __init__(self, name, surname, cpf):
        self._name = str(name).strip().title()
        self._surname = str(surname).strip().title()
        self._CPF = cpf
    
    
    @property
    def _CPF(self):
        return self._cpf
    
    
    @_CPF.setter
    def _CPF(self, value):
        value = str(value).strip().replace('.', '').replace('-', '')
        if len(value) == 11 and value.isnumeric():
            self._cpf = int(value)
        else:
            self._cpf = False


class account:
    
    number = 1111
    _numaccs = 0
    __slots__ = ['_number', '_holder', '_balance', '_limit']
    
    def __init__(self, clientcls, balance, limit=1000):
        account._numaccs += 1
        self._number = account.number
        self._Holder = clientcls
        self._balance = balance
        self._limit = limit
        account.number += 1
    
    
    @property
    def _Holder(self):
        return self._holder
    
    
    @_Holder.setter
    def _Holder(self, value):
        if type(value) == client:
            self._holder = value
        else:
            self._holder = False
    
    
    @classmethod
    def get_numaccs(cls):
        return cls._numaccs()
