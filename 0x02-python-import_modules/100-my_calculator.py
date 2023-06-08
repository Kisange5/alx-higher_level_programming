#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    ac = len(argv)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = "+-*/"
    if argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    sign = argv[2]
    b = int(argv[3])
    if sign == "+":
        print("{:d} {} {:d} = {:d}".format(a, sign, b, add(a, b)))
    elif sign == "-":
        print("{:d} {} {:d} = {:d}".format(a, sign, b, sub(a, b)))
    elif sign == "*":
        print("{:d} {} {:d} = {:d}".format(a, sign, b, mul(a, b)))
    else:
        print("{:d} {} {:d} = {:d}".format(a, sign, b, div(a, b)))
