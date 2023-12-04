#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # createss a new empty list
    new_list = []
    # checks elements in my_list
    for i in my_list:
        # checks if divisible by 2 with no remainders
        if i % 2 == 0:
            # append the result to my new_list if true
            # which is a new trick i just learnt
            new_list.append(True)
            # checks for numbers with remainders
        else:
            # append numbers with remainders also to
            # my new_list ain't that cool
            # still a lil bit confusing
            # buh we move
            new_list.append(False)
            # lastly we return our new_list
            # so it can be processed and by our main
            # voiala you results
    return new_list
