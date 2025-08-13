import math


class Shape:
    def __init__(self, length=None, width=None, radius=None):
        self.length = length
        self.width = width
        self.radius = radius

    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length=length, width=width)

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius=radius)

    def area(self):
        result = math.pi * (self.radius ** 2)
        return result
