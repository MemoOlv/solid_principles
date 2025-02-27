from typing import Protocol

class Shape(Protocol):
    def area(self) -> float:
        pass


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height
    def area(self) -> float:
        return self.width * self.height

def calculate_area(shape: Shape) -> float:
    return shape.area()
