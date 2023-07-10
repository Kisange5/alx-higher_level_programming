#!/usr/bin/python3
"""module documentation"""


def add_attribute(obj, name, data):
    """checks if attribute exists"""
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, data)
