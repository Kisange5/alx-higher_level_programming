#!/usr/bin/python3
"""module documentation"""

import json


def save_to_json_file(my_obj, filename):
    """Creates a JSON rep of an obj
    Args:
        my_obj (obj): the python obj
        filename (str): the filename/path
    Return:
          created item
    """
    with open(filename, mode='w', encoding='utf-8') as fd:
        json.dump(my_obj, fd)
