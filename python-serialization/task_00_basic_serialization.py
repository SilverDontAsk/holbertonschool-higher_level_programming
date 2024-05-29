#!/usr/bin/python3
"""
Module to serialize a python dictionary to a json file
and deserealize a json file to recreate the python dictionary
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary into a json file
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    Deserializes a json file to recreate the python dictionary
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
