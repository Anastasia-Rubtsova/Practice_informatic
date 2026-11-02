from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def food_per_day(self):
        pass

    def describe(self):
        return self.name + ": " + self.sound()


class Lion(Animal):
    def sound(self):
        return "Р-р-р"

    def food_per_day(self):
        return self.weight * 0.05


class Parrot(Animal):
    def sound(self):
        return "Привет!"

    def food_per_day(self):
        return self.weight * 0.10


class Zoo:
    def __init__(self):
        self._animals = []

    def add(self, animal):
        if isinstance(animal, Animal) == False:
            raise TypeError("Должно быть животное")
        self._animals.append(animal)

    def sounds(self):
        result = []
        for animal in self._animals:
            result.append(animal.describe())
        return result

    def total_food(self):
        total = 0
        for animal in self._animals:
            total = total + animal.food_per_day()
        return total

    def __len__(self):
        return len(self._animals)
