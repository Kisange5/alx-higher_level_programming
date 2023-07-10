#!/usr/bin/python3
"""module documentation"""


class BaseGeometry:
    """a base geometry class"""
    def area(self):
        """raises an exception error
        Raises:
              Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates an integer
        Args:
            name (str): the name
            value (int): the value to validate
        Raises:
              TypeError: {} must be an integer".format(name)
              ValueError: {} must be greater than 0".format(name)
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
