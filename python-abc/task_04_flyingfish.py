#!/usr/bin/python3
"""
Multiple Inheritance
"""


class Fish:
    """
    Fish class with fish behavior
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """
    Bird class with bird behavior
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    Class that inherits from both fish and bird classes
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
