#!/usr/bin/python3
def number_keys(a_dictionary):
    keys = list(a_dictionary)
    if keys is None:
        return None
    count = 0
    for item in keys:
        count += 1
    return count
