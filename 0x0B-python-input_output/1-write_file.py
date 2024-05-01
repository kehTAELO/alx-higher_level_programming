#!/usr/bin/python3
"""this function Defines a file-writing function """


def write_file(filename="", text=""):
    """will Write a string to a UTF8 file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
