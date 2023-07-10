#!/usr/bin/python3
"""module documentation"""


def inherits_from(obj, a_class):
    """ checks if obj is type of class that is inherited"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
