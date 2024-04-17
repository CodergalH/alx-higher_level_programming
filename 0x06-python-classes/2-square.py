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
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= zero")
        self._Square__size = size
