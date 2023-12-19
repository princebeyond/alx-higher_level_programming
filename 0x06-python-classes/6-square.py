#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square by: (based on 5-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError(
                        "position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__position[1] > 0:
            print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(' ' * self.__position[0] + "#" * self.__size)
        if self.__size == 0:
            print()
