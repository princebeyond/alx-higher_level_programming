#!/usr/bin/python3
"""Defines class rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """getter for private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """getter for private attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """getter for private attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        # return self.__width**2 + self.__height**2
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width*2 + self.__height*2
