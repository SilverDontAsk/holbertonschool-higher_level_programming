#!/usr/bin/python3
"""
Module to serialize and deserialize with XML
"""
import xml.etree.ElementTree as ET


def sanitize_tag(tag):
    return tag.replace(' ', '_')


def serialize_to_xml(dictionary, filename):
    """
    Serializes a python dictionary into an xml file
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        tag = sanitize_tag(str(key))
        item = ET.SubElement(root, tag)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserializes an xml file into an python dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}

    for child in root:
        if child.text.isdigit():
            dictionary[child.tag] = int(child.text)
        elif child.text.replace('.', '', 1).isdigit():
            dictionary[child.tag] = float(child.text)
        else:
            dictionary[child.tag] = child.text

    return dictionary
