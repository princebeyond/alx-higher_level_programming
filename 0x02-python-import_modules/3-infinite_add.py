#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    add = 0

    num = len(sys.argv)
    for i in range(1, num):
        add += int(sys.argv[i])
    print(add)
