#!/usr/bin/python3
"""module documentation"""


def is_same_class(obj, a_class):
    """checks if object isinstance of a type
    Return:
          True: if true
          False: if not
    """
    tp = type(obj)
    if tp is a_class:
        return True
    else:
        return False
