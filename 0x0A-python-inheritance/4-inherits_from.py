#!/usr/bin/python3
"""
Subs only
"""


def inherits_from(obj, a_class):
    """if the object is an instance of a class that inherited"""
    return isinstance(obj, a_class) and type(obj) != a_class
