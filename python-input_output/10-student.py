#!/usr/bin/python3
"""
Module with a Student class
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves the dictionary representation of an instance of
        student.
        """
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
