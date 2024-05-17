#!/usr/bin/python3
"""
This module defines a class Square 'size' and 'position'.
"""


class Square:
    """This is a class that defines a square by size and position"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method to access our private position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to mod the private position attribute."""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with #."""
        if self.size == 0:
            print("")
            return
        print("\n" * self.position[1], end="")
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
