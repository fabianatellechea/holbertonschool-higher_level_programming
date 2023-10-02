#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    del_keys = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            del_keys.append(k)

    for k in del_keys:
        del a_dictionary[k]

    return a_dictionary
