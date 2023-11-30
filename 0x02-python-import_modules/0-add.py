#!/usr/bin/python3

a = 1
b = 2

exec(open('add_0.py').read())

print("{} + {} = {}".format(a, b, add(a, b)))
