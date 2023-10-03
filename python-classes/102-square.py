#!/usr/bin/python3
""" creating class """


class Square:
    """ class """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    def __eq__(self, other):
        return self.__size == other.size

    def __ne__(self, other):
        return self.__size != other.size

    def __lt__(self, other):
        return self.__size < other.size

    def __le__(self, other):
        return self.__size <= other.size

    def __gt__(self, other):
        return self.__size > other.size

    def __ge__(self, other):
        return self.__size >= other.size
