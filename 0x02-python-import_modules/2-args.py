#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_arg = len(sys.argv)

    if num_arg == 1:
        print("1 argument:")
        print("{:d}: {}".format(num_arg, sys.argv[0]))
    else:
        print("{:d} arguments".format(num_arg))
        for i in range(1, num_arg):
            print("{:d}: {}".format(i, sys.argv[i]))
