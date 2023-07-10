#!/usr/bin/python3
"""module documentation"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class that inherits from rectangle"""
    def __init__(self, size):
        """instantiation of class instance"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
