#!/usr/bin/python3
"""
Module to write a string into a file
"""


def write_file(filename="", text=""):
    """
    Writes a string into a text file in UTF-8

    Returns the number of characters that are written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
