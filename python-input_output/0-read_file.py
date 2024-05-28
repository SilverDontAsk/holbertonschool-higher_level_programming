#!/usr/bin/python3
"""
Funtion to read a file and print it out to stdout
"""


def read_file(filename=""):
    """
    reads the file using a with function and prints it out to stdout
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        raise FileNotFoundError
    except IOError:
        print("Could not read from file: '{}'.".format(filename))
