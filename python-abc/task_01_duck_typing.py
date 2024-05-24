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
        self.radius = max(0, radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Rectangle class inheriting from abstract class Shape
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
