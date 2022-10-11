#!/usr/bin/python3


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
