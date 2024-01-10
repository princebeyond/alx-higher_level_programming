#!/usr/bin/python3
"""
Script that addss all arguments
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'

try:
    json_lis = load_from_json_file(filename)
except FileNotFoundError:
    json_lis = []

for arg in argv[1:]:
    json_lis.append(arg)
save_to_json_file(json_lis, filename)
