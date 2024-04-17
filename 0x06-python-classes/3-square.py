#!/usr/bin/python3
"""
Author: Glorious Oyovwuvwe Ohwojeheri <gloriousohwojeheri608@gmail.com>
Purpose: Define a Square class
"""


class Square(object):
    """ A class represents / defines a square.
    """

    def __init__(self, size=0):
        """Initialize the square with given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """
        Calculate and return the area of the square.
        :return: The area of the square as an integer.
        """
        return self._Square__size * self._Square__size
