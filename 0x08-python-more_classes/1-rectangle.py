#!/usr/bin/python3
"""
define a classs Rectangle
"""
class Rectangle:
    """this represenst the rectangle"""
    def __init__(self,width=0,height=0):
        """initializes the rectangle"""
        self.width = width
        self.height = height
    @property
    def width(self):
        """this this te getter for private instance"""
        return self.__width
    @width.setter
    def width(self,value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
@property
def height(self):
    """this is a getter for private instances"""
@height.setter
def height(self,value):
    """this is the setter for private instance"""
    if type(value) is not int:
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value
