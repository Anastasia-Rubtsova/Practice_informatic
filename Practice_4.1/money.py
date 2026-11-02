class Money:
    def __init__(self, rubles, kopecks=0):
        if rubles < 0 or kopecks < 0:
            raise ValueError("Значения не могут быть отрицательными")
        total = rubles * 100 + kopecks
        self._rubles = total // 100
        self._kopecks = total % 100

    @property
    def rubles(self):
        return self._rubles

    @property
    def kopecks(self):
        return self._kopecks

    def _to_kopecks(self):
        return self._rubles * 100 + self._kopecks

    def __add__(self, other):
        total = self._to_kopecks() + other._to_kopecks()
        return Money(0, total)

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented

    def __sub__(self, other):
        total = self._to_kopecks() - other._to_kopecks()
        if total < 0:
            raise ValueError("Результат не может быть отрицательным")
        return Money(0, total)

    def __mul__(self, other):
        if type(other) != int:
            raise TypeError("Множитель должен быть целым числом")
        if other < 0:
            raise ValueError("Множитель не может быть отрицательным")
        total = self._to_kopecks() * other
        return Money(0, total)

    def __rmul__(self, other):
        return self.__mul__(other)

    def split(self, n):
        if type(n) != int or n <= 0:
            raise ValueError("n должно быть положительным целым")
        total = self._to_kopecks()
        base = total // n
        remainder = total % n
        result = []
        for i in range(n):
            k = base
            if i < remainder:
                k = k + 1
            result.append(Money(0, k))
        return result

    def __eq__(self, other):
        return self._to_kopecks() == other._to_kopecks()

    def __lt__(self, other):
        return self._to_kopecks() < other._to_kopecks()

    def __repr__(self):
        return f"Money({self._rubles}, {self._kopecks})"

    def __str__(self):
        k = str(self._kopecks)
        if len(k) == 1:
            k = "0" + k
        return str(self._rubles) + " руб. " + k + " коп."
