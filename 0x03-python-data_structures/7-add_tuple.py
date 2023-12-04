#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = len(tuple_a)
    j = len(tuple_b)

    if i == 0:
        n_t1 = (0, 0)
    elif i == 1:
        n_t1 = tuple_a + (0,)
    else:
        n_t1 = tuple_a[:2]
    if j == 0:
        n_t2 = (0, 0)
    elif j == 1:
        n_t2 = tuple_b + (0,)
    else:
        n_t2 = tuple_b[:2]
    result_tuple = (n_t1[0] + n_t2[0], n_t1[1] + n_t2[1])
    return result_tuple
