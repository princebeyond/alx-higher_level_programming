#!/usr/bin/python3
"""
T of F
"""


def is_kind_of_class(obj, a_class):
    """if the object is an instance of, or if the object is an instance of a class"""
    if not isinstance(obj, a_class):
        return False
    else:
        return True
