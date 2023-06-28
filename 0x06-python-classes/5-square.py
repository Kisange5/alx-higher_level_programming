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

    @property
    def size(self):
        """This retrieves the size
        Return:
              The size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This sets the size attribute
        Args:
            value (int): the size of the square
        Raises:
              TypeError: size must be an integer
              ValueError: size must be >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif type(value) is int and value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This initialize the area attribute
        Return:
              Area of a square
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
