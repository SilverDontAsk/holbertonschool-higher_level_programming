#!/usr/bin/python3
"""
Module to write an object using json representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object into a text file using JSON representation
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
