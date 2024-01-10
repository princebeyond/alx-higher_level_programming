#!/usr/bin/python3
"""
Contains the read kines
"""


def read_file(filename=""):
    """Reads file content"""
    with open(filename, "r") as f:
        print(f.read(), end="")
