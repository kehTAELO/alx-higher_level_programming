#!/usr/bin/python3
"""this will Define a square-printing function"""


def print_square(size):
    """this function will Print a squarewith the # character.

    Args:
        size (int): This is the height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

