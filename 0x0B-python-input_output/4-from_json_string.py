#!/usr/bin/python3
"""
Contains Python data structure
"""

import json


def from_json_string(my_str):
    """Object (Python data structure) represented by a JSON string"""
    return json.loads(my_str)
