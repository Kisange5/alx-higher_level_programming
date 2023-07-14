#!/usr/bin/python3
"""module documentatation"""
def append_write(filename="", text=""):
    """appends a string at the end of a textfile
    Args:
        filename (str): the name of the file
        text (str): the text to be written
    Return:
          No. of characters written
    """
    with open(filename, 'a', encoding="utf-8") as fd:
        num = fd.write(text)
        return num
