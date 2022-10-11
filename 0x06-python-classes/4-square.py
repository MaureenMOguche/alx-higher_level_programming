#!/usr/bin/python3
"""defines a square object"""


class Square:
    """Defines a square object

    Attibutes:
        __size(int): defines size of one side of the square

    """

    def __init__(self, size=0):
        """initializes an instance of a square

        Args:
            size: size of one side of the square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        areasize = self.__size * self.__size
        return areasize
