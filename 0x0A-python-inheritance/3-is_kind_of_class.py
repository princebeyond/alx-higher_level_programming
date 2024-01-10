#!/usr/bin/python3
"""
T of F
"""


def is_kind_of_class(obj, a_class):
    """if the object is an instance"""
    if not isinstance(obj, a_class):
        return False
    else:
        return True
