#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # creating a sorted list
    sorted_key = sorted(a_dictionary)
    # for i in the sorted list elements
    for i in sorted_key:
        # print the dict nd the key
        print(f"{i}: {a_dictionary[i]}")
