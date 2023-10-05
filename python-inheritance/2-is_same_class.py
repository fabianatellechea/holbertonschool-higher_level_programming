#!/usr/bin/python3
""" unction that returns True if the object is
exactly an instance of the specified class """


def is_same_class(obj, a_class):
    """ function """
    if type(obj) == a_class:
        return True
    else:
        return False
