#!/usr/bin/python3
def no_c(my_string):
    n_str = ""
    no = "cC"
    for letter in my_string:
        if letter in no:
            continue
        n_str += letter
    return n_str
