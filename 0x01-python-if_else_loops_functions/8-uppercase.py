#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            print("{:s}".format(chr(ord(char) - 32)), end='', sep=' ')
    print()
