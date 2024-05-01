#!/usr/bin/python3
"""this Defines a file-appending function"""


def append_write(filename="", text=""):
    """this function Appends a string to the end of a file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The numbers of all characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
