#!/usr/bin/python3

a = 10
b = 5

exec(open('calculator_1.py').read())

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} + {} = {}".format(a, b, sub(a, b)))
print("{} + {} = {}".format(a, b, mul(a, b)))
print("{} + {} = {}".format(a, b, div(a, b)))
