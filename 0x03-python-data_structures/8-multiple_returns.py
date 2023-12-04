#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == ():
        # checking if tuple is empty with () list is []
        return 0, None
    else:
        # returns 2 at once
        return len(sentence), sentence[0]
