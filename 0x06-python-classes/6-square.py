#!/usr/bin/python3
"""A module that contains class of type square"""


class Square:
    """class Square as size"""
    def __init__(self, size=0, position=(0, 0)):
        """This initializes the size attribute
        Args:
            size (int): the size of the square
            value (tuple): the coordinates for position
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
        self.position = position

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

    @property
    def position(self):
        """gets the value of position attribute
        Return:
              the value of position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position attribute
        Args:
            value (tuple): the value to set
        """
        if type(value) is tuple and len(value) == 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """This initialize the area attribute
        Return:
              Area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square to stdout
        Return: None
        """
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
