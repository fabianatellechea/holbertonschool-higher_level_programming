#!/usr/bin/python3
""" creating class"""


class Rectangle:
    """ rectangle class"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

        if isinstance(self.__width, int) is False:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

        if isinstance(self.__height, int) is False:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if isinstance(self.__width, int) is False:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

        if isinstance(self.__height, int) is False:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        str += '#' * self.__width + "\n"
        str *= self.__height
        return str[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
