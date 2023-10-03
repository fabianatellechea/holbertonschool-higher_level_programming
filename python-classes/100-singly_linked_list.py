#!/usr/bin/python3
""" """


class Node:

    def __init__(self, data, next_node=0):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(next_node) is Node or ne

