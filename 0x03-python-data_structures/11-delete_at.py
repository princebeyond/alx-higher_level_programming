#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # i = lengthr of my list
    i = len(my_list)
    # checking of idx is negative or out of range
    if idx < 0 or idx >= i:
        # if it is it should return my_list untouched
        return my_list
    # deleting the number with it index modifying my_list
    del my_list[idx]
    # return my modified new_list
    return my_list
