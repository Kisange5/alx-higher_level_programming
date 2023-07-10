#!/usr/bin/python3
"""module documentation"""


class MyList(list):
    """class that inherits from list type
    Return:
          a sorted list
    """
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
