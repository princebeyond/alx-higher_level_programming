#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    arg_len = len(sys.argv) - 1
    if arg_len == 0:
        print('{} arguments.'.format(arg_len))
    elif arg_len == 1:
        print('{} argument:'.format(arg_len))
        print('1: {}'.format(str(sys.argv[1])))
    else:
        print('{} arguments:'.format(arg_len))
        for arg in range(1, len(sys.argv)):
            print('{}: {}'.format(arg, str(sys.argv[arg])))
