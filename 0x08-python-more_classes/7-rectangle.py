#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """private width and height attribute defined"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """property to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter to set it"""
        self.__height = value

        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ('')
        else:
            a = (str(self.print_symbol) * self.__width + "\n") * self.__height
            return a[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
