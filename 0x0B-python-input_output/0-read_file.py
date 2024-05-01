#!/usr/bin/python3
def read_file(filename=""):
    """"
    This function reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to be read. Default is an empty string.
    """

    """ Open the file in read mode ('r') with UTF-8 encoding."""
    with open('my_file_0.txt', 'r', encoding='utf-8') as file:
        """ Read the entire content of the file"""
        file_contents = file.read()

        """ Print the content to stdout."""
        print(file_contents, end="")

