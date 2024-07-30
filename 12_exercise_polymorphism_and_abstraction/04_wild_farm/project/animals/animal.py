from abc import ABC, abstractmethod
from typing import List, Type

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str,weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def allowed_food(self) -> List[Type[Food]]:
        pass

    @property
    @abstractmethod
    def weight_increment(self) -> float:
        pass

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    def feed(self, food: Food):
        if type(food) not in self.allowed_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.weight_increment
        self.food_eaten += food.quantity

