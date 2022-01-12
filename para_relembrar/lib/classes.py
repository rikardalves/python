class Human:
    def __init__(self, name):
        self.name = name
        self._life = 10
        self.damage = -2
        self._defense = 0
        self._dodge_direc = [0, 0]
        self._will_points = 0

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, value):
        self._life = value

    @property
    def dodge_direc(self):
        return self._dodge_direc

    @dodge_direc.setter
    def dodge_direc(self, value):
        places = [0, 0]
        if str(value).isnumeric():
            if 0 <= value <= 1:
                value = int(value)
                places[value] = 1
                self._dodge_direc = places

    def attack(self, target, position, modifier=0, show=False):
        from lib.prob import per

        if str(modifier).isnumeric():
            modifier = int(modifier)
        else:
            modifier = 0
        place = target.dodge_direc
        great = None
        if place[position] == 1:
            great = False
            if per(20):
                great = True
                self.damage += round((self.damage * 50 / 100))
            self.damage += modifier
            target.take_damage(self.damage)
        if show:
            if great is None:
                print('\033[31mMiss\033[m')
            elif not great:
                print('\033[32mHit!\033[m')
            else:
                print('\033[33mGreat!!\033[m')

    def take_damage(self, damage):
        self._life += damage + self._defense

    def show_life(self):
        life = ''
        for bar in range(0, self.life):
            life += '▉'
        return life

    @staticmethod
    def show_position(position):
        design = '|'
        for element in position:
            if element == 0:
                design += '   |'
            else:
                design += ' ⚔ |'
        return design


class Wizard(Human):
    def __init__(self, name):
        super().__init__(name)
        self._life = 12
        self.damage = -3


class Warrior(Human):
    def __init__(self, name):
        super().__init__(name)
        self._life = 14
        self._defense = 2
        self.damage = -2


class Ninja(Human):
    def __init__(self, name):
        super().__init__(name)
        self._life = 12
        self._defense = 1
        self.damage = -4


class Bot(Human):
    def __init__(self, name, life=10, defense=0):
        super().__init__(name)
        self.prefix = '!_bot_!'
        self.name = str(name)
        self._life = life
        self._defense = defense
        self._will_points = 0
        self.attack_chance = 50

    def dodge(self, to_return='number'):
        from lib.batalha import positions
        from random import randint

        position = randint(0, 1)
        real_position = positions(position)
        if to_return == 'list':
            return real_position
        else:
            return position

    def auto_attack(self):
        from lib import prob

        return prob.per(self.attack_chance)


def apply_class(member):
    from lib.batalha import keyboardinterrupt, line, center

    while True:
        try:
            print(f'''[1] Mago
{line()}
{center('Descrição', 53)}
Um ágil combatente supreendentemente silencioso e 
astuto. Não tem uma resistência alta, porém o peso
de seus golpes pode derruba os mais fortes guerreiros
{line()}
[2] Guerreiro
[3] Ninja''')
            character_class = int(input('Escolha uma das classes acima: '))

            if 0 < character_class <= 3:
                if character_class == 1:
                    member = Wizard(member)
                elif character_class == 2:
                    member = Warrior(member)
                elif character_class == 3:
                    member = Ninja(member)
                return member
        except KeyboardInterrupt:
            keyboardinterrupt()
        except ValueError:
            continue

# Elementos
