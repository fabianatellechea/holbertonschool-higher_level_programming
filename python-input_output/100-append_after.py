#!/usr/bin/python3
""" nserts a line of text to a file, after each line
containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """function """
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
