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


class SavingsAccount(Account):
    def __init__(self, number, owner, balance=0, rate=0.05):
        super().__init__(number, owner, balance)
        self._rate = rate

    @property
    def rate(self):
        return self._rate

    def add_interest(self):
        self._balance = self._balance + self._balance * self._rate

    def __repr__(self):
        return f"SavingsAccount('{self._number}', '{self._owner}', {self._balance}, {self._rate})"


class CheckingAccount(Account):
    def __init__(self, number, owner, balance=0, overdraft=0):
        super().__init__(number, owner, balance)
        self._overdraft = overdraft

    @property
    def overdraft(self):
        return self._overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if self._balance - amount < -self._overdraft:
            raise ValueError("Превышен овердрафт")
        self._balance = self._balance - amount

    def __repr__(self):
        return f"CheckingAccount('{self._number}', '{self._owner}', {self._balance}, {self._overdraft})"
