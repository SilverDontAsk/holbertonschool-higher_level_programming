#!/usr/bin/python3
"""
This function returns true if obj is instance of inherited class
otherwise false
"""


def inherits_from(obj, a_class):
    """
    Returns true if obj is an instance of a class that
    inherited in the specified class
    otherwise false

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        true if obj instance of a class inherited in a_class
        false otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
