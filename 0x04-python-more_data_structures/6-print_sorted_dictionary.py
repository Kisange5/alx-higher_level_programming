#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_alpha = sorted(a_dictionary.keys())
    for items in keys_alpha:
        value = a_dictionary[items]
        print("{}: {}".format(items, value))
