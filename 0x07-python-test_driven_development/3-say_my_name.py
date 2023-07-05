#!/usr/bin/python3
"""module documentation"""


def say_my_name(first_name, last_name=""):
    """prints a strin with first name and last name
    Args:
        first_name (str): first name
        last_name (str): mlast name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f'My name is {first_name} {last_name}')
