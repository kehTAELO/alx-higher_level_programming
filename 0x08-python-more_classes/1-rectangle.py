#!/usr/bin/python3
class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height
    @property
    def width(self):
        "this method returns value of width"
        return self.__width
    @width.setter
    def width(self,value):
        "method will define height and also raise Errors"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

@property
"this method returns value of height"
def height(self):
    return self.__height
@height.setter
"method defines height and raises typeError and ValueError"
def height(self,value):
    if type(value) != int:
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value
