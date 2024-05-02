#!/usr/bin/python3
"""this function will Define an integer addition"""


def add_integer(a, b=98):
    """this will Return the integer addition of a and b.
    Raises:
        TypeError: if a and b are not  integers or floats.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

