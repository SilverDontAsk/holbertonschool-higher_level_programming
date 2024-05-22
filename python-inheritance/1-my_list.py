#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
"""


class MyList(list):
    """
    MyList class that inherits from list.

    Methods:
        print_sorted: prints the list
    """
    
    def print_sorted(self):
        """
        Prints list in an ascending sorted order
        """
        print(sorted(self))
