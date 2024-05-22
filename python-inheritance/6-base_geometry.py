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
