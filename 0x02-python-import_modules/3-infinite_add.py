#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg_sum = 0
    arg_len = len(sys.argv)

    for i in range(1, arg_len):
        arg_sum += int(sys.argv[i])
    print('{:d}'.format(arg_sum))
