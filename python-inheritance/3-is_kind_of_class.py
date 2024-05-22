#!/usr/bin/python3
"""
This function returns true if obj is an instance of or if
obj is an instance of a class, otherwise false
"""


def is_kind_of_class(obj, a_class):
    """
    returns true if object is an instance of class or
    a class that is inherited of a specified class
    false otherwise
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
