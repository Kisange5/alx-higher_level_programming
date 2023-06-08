#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    ac = len(argv) - 1
    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print("{:d} argument:".format(ac))
        print("{:d}: {}".format(ac, argv[1]))
    else:
        print("{:d} arguments:".format(ac))
        num = 1
        while num < ac + 1:
            print("{:d}: {}".format(num, argv[num]))
            num += 1
