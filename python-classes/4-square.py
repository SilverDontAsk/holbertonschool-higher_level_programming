#!/usr/bin/python3
"""
This module defines a class Square 'size'.
"""


class Square:
    """This is a class that defines a square by size"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter method to access our private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to mod the private size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns area of square"""
        return self.__size ** 2
