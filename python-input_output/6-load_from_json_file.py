#!/usr/bin/python3
"""
Module that creates an object from JSON file
"""

import json


def load_from_json_file(filename):
    """
    Creates an object in a JSON file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
