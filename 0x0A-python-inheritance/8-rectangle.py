#!/usr/bin/python3
"""
Contains class base---
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of rect"""
    def __init__(self, width, height):
        """instantion of a rect"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
