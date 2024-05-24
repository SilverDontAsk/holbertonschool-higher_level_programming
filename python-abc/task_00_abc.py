#!/usr/bin/python3
"""
Abstract Animal Class
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal Class with abstract subclasses
    """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """
    Dog class that inherits abstract class Animal
    """
    def sound(self):
        """
        sound method for dog class
        """
        return "Bark"

class Cat(Animal):
    """
    Cat class that inherits abstract class Animal
    """
    def sound(self):
        """
        sound method for cat class
        """
        return "Meow"
