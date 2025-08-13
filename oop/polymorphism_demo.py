import math


class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self, length, width):
        return length * width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self, radius):
        result = math.pi * (radius * radius)
        return result
