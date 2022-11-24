from abc import ABC, abstractmethod
import random


class Animal(ABC):
    def __init__(self, name, age=1, gender="unknown"):
        self.name = name
        self.age = age
        self.gender = gender
        self.fedTimes = 0

    def eat(self):
        self.fedTimes += 1
        return self.fedTimes

    @abstractmethod
    def isHungry(self):
        pass

    def __str__(self):
        return f'{self.name} is a {self.age} years old {self.gender} animal and was fed {self.fedTimes} times'


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    def isHungry(self):
        return True


class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)

    def isHungry(self):
        hungry = random.choice([True, False])
        return hungry


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    def isHungry(self):
        if self.fedTimes % 2 == 0:
            return True
        else:
            return False


class Worker():
    def __init__(self, name, animalsToLookAfter=None):
        if animalsToLookAfter is None:
            self._animalsToLookAfter = []
        else:
            self._animalsToLookAfter = animalsToLookAfter
        self.name = name

    @property
    def animalsToLookAfter(self):
        return self._animalsToLookAfter

    @animalsToLookAfter.setter
    def animalsToLookAfter(self, new_list):
        self._animalsToLookAfter = new_list

    def add_animal(self, Animal):
        animal_ls = Animal
        self._animalsToLookAfter.append(animal_ls)

    def doDailyRoutine(self):
        for animal in self._animalsToLookAfter:
            if animal.isHungry():
                animal.eat()
            else:
                continue
