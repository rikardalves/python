# ATENÇÃO! getters e setters devem ser usados só quando necessário, esse documento é para treinamento
def replace_list(var, characters, new):
    var = str(var)
    for character in characters:
        var = var.replace(character, new)
    return var


class Product:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    
    @property
    def value(self):
         return self._value
    
    
    @value.setter
    def value(self, value):
        try:
            value = replace_list(value, ('$', 'r', ' ', '-'), '')
            value = value.replace(',', '.')
            value = float(value)
        except:
            value = 0
        self._value = value
    
    
    @property
    def name(self):
        return self._name
    
    
    @name.setter
    def name(self, name):
        name = str(name).capitalize().strip()
        self._name = name
    
    
    def increase(self, percentage):
        # Variável a.value deve receber este método
        result = self.value + (self.value * percentage / 100)
        return result
    
    
    def reduction(self, percentage):
        # Estem método não ser recebido por uma variável
        self.value = self.value - (self.value * percentage / 100)
        return self.value
