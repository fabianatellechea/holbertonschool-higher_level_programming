#!/usr/bin/python3
""" creating class """


class Square:
    """ class """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) == tuple and len(position) == 2:
            for value in position:
                if type(value) != int or value < 0:
                    raise TypeError(
                            "position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if type(i) is not int or i < 0:
                raise TypeError(
                        "position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):

        if self.__size == 0:
            print()

        if self.__position[1] > 0 and self.__size > 0:
            for i in range(self.__position[1]):
                print()

        for i in range(self.__size):
            print(' ' * self.__position[0], end="")
            print('#' * self.__size)
