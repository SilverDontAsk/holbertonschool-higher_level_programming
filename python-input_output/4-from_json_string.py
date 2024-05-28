#!/usr/bin/python3
"""
Module to return an object in JSON
"""

import json


def from_json_string(my_str):
    """
    Returns an object in json format
    """
    return json.loads(my_str)
