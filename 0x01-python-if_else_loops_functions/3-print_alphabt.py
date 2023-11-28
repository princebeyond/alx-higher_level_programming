#!/usr/bin/python3
for ac in range(97, 123):
    if chr(ac) == 'q' or chr(ac) == 'e':
        continue
    print("{}".format(chr(ac)), end='', sep='')
