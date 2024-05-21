#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    Represents a rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        Rectangle.number_of_instances += 1

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            int: area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimiter of the rectangle

        Returns:
            int: the perimeter of the triangle

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle with #.

        Returns:
            str: the string representation of the rectangle.

        """
        if self.__width == 0 or self.__height == 0:
            return ""
        if not isinstance(self.print_symbol, str):
            self.print_symbol = str(self.print_symbol)
        rectangle = []
        for _ in range(self.__height):
            rectangle.append(self.print_symbol * self.__width)
        return '\n'.join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle

        Returns:
            str: a string representation of the rectangle object.

        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when the rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on its area

        Args:
            rect_1: the first rectangle
            rect_2: the second rectangle

        Returns:
            Rectangle: the rectangle with the greatest area.
            returns rect_1 is both are the same.

        Raises:
            TypeError: when rect_1 or 2 isnt an instance of rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
