from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.__radius


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_perimeter(self):
        return 2 * (self.__length + self.__width)

    def calculate_area(self):
        return self.__length * self.__width



