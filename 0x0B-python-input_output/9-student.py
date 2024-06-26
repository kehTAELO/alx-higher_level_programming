#!/usr/bin/python3
"""Defines a class Student"""

class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """this function will Initialize a new Student.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
             """this will Get a dictionary representation of the Student."""
             return self.__dict__
