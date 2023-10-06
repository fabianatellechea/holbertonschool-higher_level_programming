#!/usr/bin/python3
"""creating class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
