#!/usr/bin//python3
def safe_print_integer(value):
    # using try blocks
    try:
        # checking if value is int
        check = int(value)
        # printing value that is int
        print("{:d}".format(check))
        # returns true if vaue is int
        return True
    # handling thr valueerror it make if not
    except ValueError:
        # returns false if value not int
        return False
