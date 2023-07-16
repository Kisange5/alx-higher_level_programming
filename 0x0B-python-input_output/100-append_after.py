#!/usr/bin/python3
"""module documentation for insertion of a text in a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of  text to a file after
    each line containing a specific string
    """
    text = ""
    with open(filename) as fd:
        for line in fd:
            text = text + line
            if search_string in line:
                text = text + new_string

    with open(filename, "w") as fd:
        fd.write(text)
