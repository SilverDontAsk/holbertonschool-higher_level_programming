#!/usr/bin/python3
def print_square(size):
    """
    Prints a square of size x size with '#'.

    Args:
    size (int): Size of the square. Must be an int and > 0.

    Raises:
    TypeError: If size is not an int.
    TypeError: If size is a float and less than 0.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
