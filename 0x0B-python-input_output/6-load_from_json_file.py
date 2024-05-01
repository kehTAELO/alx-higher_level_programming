#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """this function Creates a Python object"""
    with open(filename) as f:
        return json.load(f)
