#!/usr/bin/python3
"""Defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """this function Creates a Python object"""
    with open(filename) as f:
        return json.load(f)
