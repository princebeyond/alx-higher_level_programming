#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # creating an empty new_list needed
    new_list = []
    # send an undercover agent which is i to go fishing for search
    # for i in my list
    for i in my_list:
        # i fishing for the imposter search
        # if i equals search
        if i == search:
            # when i finds the imposter he replace's him with the original
            # which in our case is replace
            # if i equals search it should append replace to it instead
            new_list.append(replace)
            # when the imposter has been replaced
            # if search can't be found
        else:
            # it should still add the nxt number to new_list
            # so it will be able to print the full list
            # appending the next number in the list
            new_list.append(i)
            # once i is done replacing and add nxt numbers
            # we return our new_list to our main
    return new_list
