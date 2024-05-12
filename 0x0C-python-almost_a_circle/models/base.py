#!/usr/bin/python3
"""this are the models for the base class"""

class Base:
    """the private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base__nb_objects = + 1
            self.id = Base.__nb_objects

