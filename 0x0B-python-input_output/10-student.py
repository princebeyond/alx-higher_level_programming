#!/usr/bin/python3
"""
Class Student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Method to initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            dic = {}
            for i in attrs:
                if i in self.__dict__:
                    dic[i] = self.__dict__[i]
            return dic
        else:
            return self.__dict__.copy()
