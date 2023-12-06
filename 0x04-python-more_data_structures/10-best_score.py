#!/usr/bin/python3
def best_score(a_dictionary):
    # checking if dict ids none to return noone
    if a_dictionary is None:
        return None
    # getting the maximum value in dict and the key to it
    maximuim_key = max(a_dictionary, key=a_dictionary.get)
    # returns maximuim_key
    return maximuim_key
