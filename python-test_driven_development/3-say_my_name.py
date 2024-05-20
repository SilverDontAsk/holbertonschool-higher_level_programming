#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints the formatted name.

    If last_name is not found, only first_name is printed.

    Raises:
        TypeError: if first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
