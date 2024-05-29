#!/usr/bin/python3
"""
Module to serialize and deserialize with XML
"""
import xml.etree.ElementTree as ET



def serialize_to_xml(dictionary, filename):
    """
    Serializes a python dictionary into an xml file
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, "item", key=key)
        item.text = str(value)

    tree = ET.ElementsTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Deserializes an xml file into an python dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}

    for item in root.findall("item"):
        key = item.get("key")
        value = item.text

        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except ValueError:
                pass

        dictionary[key] = value

    return dictionary
