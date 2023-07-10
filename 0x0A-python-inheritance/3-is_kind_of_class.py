#!/usr/bin/python3
"""module documentation"""


def is_kind_of_class(obj, a_class):
    """checks if obj isintance of type or parent type"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
