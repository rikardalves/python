from library.prob import *


class Human:
    __slots__ = ['_name', '_life', '_damage']

    def __int__(self, name, life, damage):
        self._name = name
        self._life = life
        self._damage = damage

    @property
    def damage(self):
        probability = per(20)
        if probability:
            critical = int((self.damage * 50) / 100)
        else:
            critical = 0
        return self.damage + critical

    @damage.setter
    def damage(self, value):
        self._damage = value

    def attack(self, target):
        pass
