#!/usr/bin/python3
"""
Module to serialize and deserialize with the pickle module
"""
import pickle


class CustomObject:
    """
    Custom Object class with name, age, is_student
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        serializes with the pickle module
        """
        try:
            with open(filename, 'wb') as pickle_file:
                pickle.dump(self, pickle_file)
        except Exception as p:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes with the pickle module
        """
        try:
            with open(filename, 'rb') as pickle_file:
                return pickle.load(pickle_file)
        except Exception as p:
            return None
