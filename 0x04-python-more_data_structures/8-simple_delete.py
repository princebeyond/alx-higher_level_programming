#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # checking if key is in the a_dictionary so it will clear the error
    # it was giving me before
    if key in a_dictionary:
        # if key is there it deletes if not nothing changes
        del a_dictionary[key]
        # as usual return it
    return a_dictionary
