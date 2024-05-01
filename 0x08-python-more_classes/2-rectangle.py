#!/usr/bin/python3
"""this will define a rectangle"""
class Rectangle:
    """represents the rectangle"""
    def __init__(self,width=0, height=0):
        """this will initialize the rectangle"""
        self.width = width
        self.height = height
        @property
        def width(self):
           """this is the getter for a private intsance"""
           return self.__width
        
        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

    
        @property
        def height(self):
            """this is the getter for the private instances"""
            return self.__height
        @height.setter
        def height(self,value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        
    def area(self):
            """this will return the area of the ractangle"""
            return self.__width * self.__height
    def perimeter(self):
        """this will return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)
