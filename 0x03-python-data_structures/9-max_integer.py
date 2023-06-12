#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    maxV = my_list[0]
    for item in my_list:
        if item > maxV:
            maxV = item
    return maxV
