#!/usr/bin/python3
"""module documentation"""


class MyList(list):
    """class that inherits from list type
    Return:
          a sorted list
    """
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
