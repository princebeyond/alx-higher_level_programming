#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(0, 5):
        my_list.reverse()
        print("{}".format(my_list[i]), end='')
        print()
