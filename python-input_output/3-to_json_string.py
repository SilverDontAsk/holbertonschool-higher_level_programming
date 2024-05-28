#!/usr/bin/python3
"""
Module to return the json representation of a string
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a string
    """
    return json.dumps(my_obj)
