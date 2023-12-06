#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # setting set to 1 of em
    first = set(set_1)
    # element in set_1 or set_2 but not in both
    return first ^ set_2
