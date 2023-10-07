#!/usr/bin/python3
""" appends a string at the end of a text file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """function """
    with open(filename, 'a') as f:
        return f.write(text)