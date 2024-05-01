#!/usr/bin/python3
"""this will Define a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """this function will Return the JSON representation."""
    return json.dumps(my_obj)
