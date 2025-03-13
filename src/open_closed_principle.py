from typing import Protocol
from math import pi


class Shape(Protocol):
    def area(self) -> float:
        pass


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height

    def area(self) -> float:
        return self.width * self.height


class Circle:
    def __init__(self, radius: float):
        self.radius: float = radius

    def area(self) -> float:
        return pi * (self.radius**2)


def calculate_area(shape: Shape) -> float:
    return shape.area()
