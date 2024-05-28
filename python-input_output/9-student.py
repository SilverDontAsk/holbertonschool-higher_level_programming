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

    def to_json(self):
        """
        Retrieves the dictionary representation of an instance of
        student.
        """
        return self.__dict__
