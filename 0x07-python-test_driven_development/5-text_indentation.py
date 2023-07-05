#!/usr/bin/python3
"""module documentation"""


def text_indentation(text):
    """prints a text with 2 new lines after\
        each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    sp = 0
    for c in text:
        if sp == 0:
            if c == ' ':
                continue
            else:
                sp = 1
        if sp == 1 and c in ".?:":
            print(c)
            print()
            sp = 0
        else:
            print(c, end='')
