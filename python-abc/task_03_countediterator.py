#!/usr/bin/python3
"""
Keeping track of iteration
"""


class CountedIterator:
    """
    keeps track of the number of items that have been iterated
    """

    def __init__(self, iter_obj):
        self.iter_obj = iter(iter_obj)
        self.obj_count = 0

    def get_count(self):
        """
        Returns the current count of iterations
        """
        return self.obj_count

    def __iter__(self):
        return self

    def __next__(self):
        """
        Grabs the next item and increments the counter.
        """
        item = next(self.iter_obj)
        self.obj_count += 1
        return item
