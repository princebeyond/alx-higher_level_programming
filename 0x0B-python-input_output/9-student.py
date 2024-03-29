#!/usr/bin/python3
"""
Class Student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """defines a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation"""
        return self.__dict__.copy()
