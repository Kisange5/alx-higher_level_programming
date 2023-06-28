#!/usr/bin/python3
"""A module that contains class of type square"""


class Square:
    """class Square as size"""
    def __init__(self, size=0):
        """This initializes the size attribute
        Args:
            size (int): the size of the square
        Raises:
              TypeError: size must be an integer
              ValueError: size must be >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif type(size) is int and size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
