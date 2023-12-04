#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        # if my_list is empty
        return None
    my_list.sort()
    # sort in accending order and return [-1] last number
    return my_list[-1]
