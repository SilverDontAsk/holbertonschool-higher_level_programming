#!/usr/bin/python3

def lookup(obj):
    """Returns the list of available attributes and methods of obj

    Parameters:
        obj: this is the object to inspect.

    Returns:
        list: a list of strings that represent an attribute or method.
    """
    return list(dir(obj))
