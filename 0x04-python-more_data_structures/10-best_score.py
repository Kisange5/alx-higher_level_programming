#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    marks = 0
    name = ""
    for keys in a_dictionary:
        if a_dictionary[keys] >= marks:
            marks = a_dictionary[keys]
            name = keys
    if marks == 0:
        return None
    else:
        return name
