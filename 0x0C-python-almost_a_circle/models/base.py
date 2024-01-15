#!/usr/bin/python3
"""
Class Base
"""


import json
import csv
import turtle


class Base:
    """Represent Base model"""

    __nb_object = 0


    def __init__(self, id=None):
        """Initialize a new base"""
        if id is not None:
            self.id = id
        else:
            Base.___nb_objects += 1
            self.id = Base.___nb_objects
