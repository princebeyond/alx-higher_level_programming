#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square by: (based on 4-square.py)"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        # self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        are = self.__size * self.__size
        return are

    def my_print(self):
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
