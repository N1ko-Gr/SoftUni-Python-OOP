from abc import ABC
from typing import List, Type

from project.animals.animal import Animal
from project.food import Food, Vegetable, Fruit, Meat


class Mammal(Animal, ABC):
    def __init__(self,name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Mouse(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Vegetable, Fruit]

    @property
    def weight_increment(self) -> float:
        return 0.10

    @staticmethod
    def make_sound():
        return 'Squeak'


class Dog(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 0.40

    @staticmethod
    def make_sound():
        return 'Woof!'


class Cat(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat, Vegetable]

    @property
    def weight_increment(self) -> float:
        return 0.30

    @staticmethod
    def make_sound():
        return 'Meow'


class Tiger(Mammal):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_increment(self) -> float:
        return 1.00

    @staticmethod
    def make_sound():
        return 'ROAR!!!'


