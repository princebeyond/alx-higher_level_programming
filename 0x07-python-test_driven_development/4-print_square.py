#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """size of square to be printed"""
    if not isinstance(size, int):
        raise TypeError ("size must be an integer")
    if size < 0:
        raise ValueError ("size must be >= 0")
    # if type(size) is float and size < 0:
        # raise ValueError ("size must be an integer")
    print(("#" * size + "\n") * size, end="")
