#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(check))
        return True
    except (TypeError, ValueError):
        return False
