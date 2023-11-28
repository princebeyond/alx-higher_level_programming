#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digits = number % 10 if number >= 0 else -(-number % 10)
if Last_digits > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, Last_digits))
elif Last_digits == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, Last_digits))
elif Last_digits < 6 and Last_digits != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, Last_digits))
