#!/usr/bin/python3
"""
This function returns true if object is exactly a specified class
otherwise false.
"""


def is_same_class(obj, a_class):
    """
    Returns True object is exactly of the specified class
    otherwise false

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True is obj is an instance of a_class, otherwise false
    """
    return type(obj) == a_class
