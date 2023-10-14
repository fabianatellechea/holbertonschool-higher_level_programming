#!/usr/bin/python3
"""creating class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading method """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.height}'

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        attrs = ['id', 'size', 'x', 'y']

        if args:
            for i in range(len(args)):
                if i < len(attrs):
                    setattr(self, attrs[i], args[i])
        for key, value in kwargs.items():
            if key in attrs:
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square """
        return {
                'id': self.id,
                'size': self.height,
                'x': self.x,
                'y': self.y
                }
