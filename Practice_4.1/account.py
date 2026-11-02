class Account:
    def __init__(self, number, owner, balance=0):
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._number = number
        self._owner = owner
        self._balance = balance

    @property
    def number(self):
        return self._number

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance = self._balance + amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if self._balance < amount:
            raise ValueError("Недостаточно средств")
        self._balance = self._balance - amount

    def __repr__(self):
        return f"Account('{self._number}', '{self._owner}', {self._balance})"
