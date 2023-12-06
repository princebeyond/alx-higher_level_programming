#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # creating an empty list not really needed
    new_matrix = []
    # map function applies its lambda function to each row in the matrix
    # The lambda function itself contains another map function, which
    # applies its lambda function to each i in the row squaring it.
    new_matrix = list(map(lambda row:
                          list(map(lambda i: i ** 2, row)), matrix))
    return new_matrix
