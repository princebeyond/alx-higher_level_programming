#!/bin/usr/python3
"""
File to overwrite, write, or create
"""


def write_file(filename="", text=""):
    """Writes to the file"""
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
