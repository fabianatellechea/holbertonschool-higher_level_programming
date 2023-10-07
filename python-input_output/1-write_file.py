#!/usr/bin/python3
""" a string to a text file (UTF8) and returns the number of characters"""


def write_file(filename="", text=""):
    """function """
    with open(filename, 'w') as f:
        return f.write(text)
