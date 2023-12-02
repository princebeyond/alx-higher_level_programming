#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list[:]
    if idx < 0:
        return copied_list
    i = len(my_list)
    if idx >= i:
        return copied_list
    copied_list[idx] = element
    return copied_list
