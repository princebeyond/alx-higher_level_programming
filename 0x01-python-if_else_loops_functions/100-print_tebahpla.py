#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    case = chr(i).lower() if i % 2 == 0 else chr(i).upper()
    print(f"{case}", end='')
