#!/usr/bin/python3
"""module documentation"""


import json


def from_json_string(my_str):
    """creates an object from str
    Args:
         my_str (str): the python object
    Return:
          the created item
    """
    py_obj = json.loads(my_str)
    return py_obj
