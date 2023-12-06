#!/usr/bin/python3
def uniq_add(my_list=[]):
    # set a function that removes Re-ocurring elements
    uniq_num = set(my_list)
    # add = 0 a lil trick i learnt during argv project
    add = 0
    # for i in uniq_num is litraly i being the elements in uniq_num
    for i in uniq_num:
        # add is 0 so a perfect way to add them all together
        add += i
        # as at the time i was so confued on how why is my answer 15
        # i add to check my uniq_num
    # print(uniq_num)
    # finnally we return add to the bosss main
    return add
