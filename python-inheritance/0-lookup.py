#!/usr/bin/python3
"""
This module defines the loopup function that will return a list of
available attributes and methods of an object.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of obj

    Parameters:
        obj: this is the object to inspect.

    Returns:
        list: a list of strings that represent an attribute or method.
    """
    return list(dir(obj))
