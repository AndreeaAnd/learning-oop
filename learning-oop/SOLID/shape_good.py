from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('circle')
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__('rectangle')
        self.width=width
        self.height=height

    def calculate_area(self):
        return self.width * self.height

# super - chemi clasa parinte


class Square(Rectangle):
    def __init__(self, side):
        super(Rectangle, self).__init__('square')
        super().__init__(side, side)
        self.side=side


c = Circle(2)
print(c.calculate_area())

r=Rectangle(2, 3)
print(r.calculate_area())

sq=Square(5)
print(sq.calculate_area())



