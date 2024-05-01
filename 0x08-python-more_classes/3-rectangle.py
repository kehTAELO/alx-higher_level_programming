#!/usr/bin/python3
# This is the Rectangle class
class Rectangle:
    # The __init__ method initializes the Rectangle instance with width and height values
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # This is the getter for the private instance attribute __width
    @property
    def width(self):
        return self.__width

    # This is the setter for the private instance attribute __width
    @width.setter
    def width(self, value):
        # Check if the value is an integer
        if type(value) != int:
            raise TypeError("width must be an integer")
        # Check if the value is greater than 0
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # This is the getter for the private instance attribute __height
    @property
    def height(self):
        return self.__height

    # This is the setter for the private instance attribute __height
    @height.setter
    def height(self, value):
        # Check if the value is an integer
        if type(value) != int:
            raise TypeError("height must be an integer")
        # Check if the value is greater than 0
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # This method returns the area of the rectangle
    def area(self):
        return self.__width * self.__height

    # This method returns the perimeter of the rectangle
    def perimeter(self):
        # If either width or height is 0, return 0
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    # This method returns a string representation of the rectangle using the '#' character
    def __str__(self):
        # If either width or height is 0, return an empty string
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

