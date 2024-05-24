#!/usr/bin/python3
"""
Abstract Class Shape
"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Shape class inheriting ABC
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """
    Circle class inheriting from abstract class Shape
    """
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius must be greater than 0")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Rectangle class inheriting from abstract class Shape
    """
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be greater than 0")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
