#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # create an empty dict
    new_dict = {}
    # a new fuction learnt .items
    for key, value in a_dictionary.items():
        # multiply the value ignore the lambda code me trying sth
        # new_dict = list(map(lambda a_dictionary[i]: i * 2, a_dictionary))
        new_dict[key] = value * 2
        # as usual return the new dict
    return new_dict
