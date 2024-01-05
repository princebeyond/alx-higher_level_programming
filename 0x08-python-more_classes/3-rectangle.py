#!/usr/bin/python3
"""Defines a class rectangle"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """setter for a private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """getter for a private attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """setter for a private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """getter to private attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height*2 + self.__width*2

    def __str__(self):
        """returns printable string"""
        s = ""
        if self.__width != 0 and self.__height != 0:
            s += "\n".join("#" * self.__width
                           for j in range(self.__height))
            return s
