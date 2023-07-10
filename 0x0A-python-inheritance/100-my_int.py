#!/usr/bin/python3
"""module documentation"""


class MyInt(int):
    """class that inherits from int"""
    def __init__(self, num):
        """class initializer"""
        self.num = num
        super().__init__()

    def __eq__(self, num2):
        """checks whether nums are equal"""
        if self.num == num2:
            return False
        else:
            return True

    def __ne__(self, num2):
        """checks whether nums are not equal"""
        if self.num != num2:
            return False
        else:
            return True
