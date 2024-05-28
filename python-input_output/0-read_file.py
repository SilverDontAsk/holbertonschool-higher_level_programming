#!/usr/bin/python3
"""
Funtion to read a file and print it out to stdout
"""


def read_file(filename=""):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("{} not found.".format(filename))
    except IOError:
        print("Could not read from file: '{}'.".format(filename))
