#!/usr/bin/python3
"""this will Define a JSON-to-object"""
import json

def from_json_string(my_str):
    """this function Returns the Python object representation """
    return json.loads(my_str)
