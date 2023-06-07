#!/usr/bin/python3

def uppercase(str):
    nstr = ""
    for char in str:
        val = ord(char)
        if val >= 97 and val <= 122:
            val = val - 32
            nstr += chr(val)
        else:
            nstr += chr(val)
    print("{}".format(nstr))
