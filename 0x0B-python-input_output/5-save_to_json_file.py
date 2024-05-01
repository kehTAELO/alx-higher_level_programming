#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """this function will Write an object to a text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
