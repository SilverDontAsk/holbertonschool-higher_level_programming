#!/usr/bin/python3
"""
This is a BaseGeometry class module
"""


class BaseGeometry:
    """
    Class used to represent a base geometry
    """
    def area(self):
        """
        Raises an exception to indicate that the area method
        is not implement
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.

        Raises:
            TypeError; if value is not an int
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
