from abc import ABC

from project.animals.animal import Animal
from project.food import Meat, Vegetable, Fruit, Seed


class Bird(Animal, ABC):
    def __init__(self, name: str,weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Owl(Bird):

    @property
    def weight_increment(self):
        return 0.25

    @property
    def allowed_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'


class Hen(Bird):
    @property
    def allowed_food(self):
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def weight_increment(self):
        return 0.35

    @staticmethod
    def make_sound():
        return 'Cluck'

