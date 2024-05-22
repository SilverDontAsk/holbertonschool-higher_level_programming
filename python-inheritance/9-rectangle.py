#!/usr/bin/python3
"""
This class rectangle inherits from class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from class BaseGeometry
    """
    def __init__(self, width, height):
        """
        initializes the rectangle with given height and width
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Defines the string representation of Rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
