#!/usr/bin/python3
"""
This module defines a class Square 'size'.
"""


class Square:
    """This is a class that defines a square by size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")
