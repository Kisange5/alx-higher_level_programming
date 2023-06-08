#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    ac = len(argv)
    if ac == 1:
        print("0")
    elif ac == 2:
        print("{:d}".format(int(argv[1])))
    else:
        num = 0
        total = 0
        while ac > 1:
            num = int(argv[ac - 1])
            total += num
            ac -= 1
        print(total)
