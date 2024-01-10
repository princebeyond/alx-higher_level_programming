#!/usr/bin/python3
"""
Contains file to copy
"""


import json


def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON representation"""
    with open(filename, 'w') as f:
        j_string = json.dumps(my_obj)
        f.write(j_string)
