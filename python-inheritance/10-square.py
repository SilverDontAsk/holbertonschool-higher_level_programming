#!/usr/bin/python3
"""
Thie module represents a class square that inherits from class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Class that inherits from class rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        calclates the size of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        return square description
        """
        return f"[Square] {self.__size}/{self.__size}"
