#!/usr/bin/python3
"""
Module to read CSV and convert it into JSON 
using serialization techniques
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Converts CSV into JSON
    """
    try:
        with open(filename, mode='r') as csv_file:
            csv_read = csv.DictReader(csv_file)
            data = [row for row in csv_read]

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
    except Exception as p:
        return False
