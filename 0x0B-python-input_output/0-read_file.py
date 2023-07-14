#!/usr/bin/python3
"""module documentation"""


def read_file(filename=""):
    """reads a text file
    Args:
        filename (str): the name of the file
    """
    with open(filename, encoding="utf-8") as fd:
        data = fd.read()
        print(data, end="")
