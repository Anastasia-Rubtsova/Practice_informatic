class Hero:
    def __init__(self, name):
        self.name = name
        self._level = 1
        self._xp = 0
        self._max_hp = 100
        self._hp = 100

    @property
    def level(self):
        return self._level

    @property
    def xp(self):
        return self._xp

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def hp(self):
        return self._hp

    @property
    def is_alive(self):
        return self._hp > 0

    def _check_alive(self):
        if self._hp <= 0:
            raise ValueError("Герой мёртв")

    def gain_xp(self, points):
        self._check_alive()
        if points <= 0:
            raise ValueError("Опыт должен быть положительным")
        self._xp = self._xp + points
        while self._xp >= 100 * self._level:
            self._xp = self._xp - 100 * self._level
            self._level = self._level + 1
            self._max_hp = 100 + (self._level - 1) * 20
            self._hp = self._max_hp

    def take_damage(self, amount):
        self._check_alive()
        if amount <= 0:
            raise ValueError("Урон должен быть положительным")
        new_hp = self._hp - amount
        if new_hp < 0:
            new_hp = 0
        self._hp = new_hp

    def heal(self, amount):
        self._check_alive()
        if amount <= 0:
            raise ValueError("Лечение должно быть положительным")
        new_hp = self._hp + amount
        if new_hp > self._max_hp:
            new_hp = self._max_hp
        self._hp = new_hp

    def attack(self, other):
        self._check_alive()
        if other._hp <= 0:
            raise ValueError("Нельзя атаковать мёртвого")
        if self is other:
            raise ValueError("Нельзя атаковать себя")
        other.take_damage(20)
        if other._hp <= 0:
            self.gain_xp(50 * other._level)

    def __repr__(self):
        return f"Hero('{self.name}', level={self._level}, xp={self._xp}, hp={self._hp}/{self._max_hp})"
