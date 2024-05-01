#!/usr/bin/python3
"""Defines a text file insertion function.victor"""


def append_after(filename="", search_string="", new_string=""):
    """this function Insert text after each line.

    Args:
        filename (str): filename.
        search_string (str): string to search for within the file.
        new_string (str): string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
