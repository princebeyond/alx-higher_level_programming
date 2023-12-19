#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square by: (based on 3-square.py)"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        loca = self.__size * self.__size
        return loca
