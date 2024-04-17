#!/usr/bin/python3
"""
Author: Glorious Oyovwuvwe Ohwojeheri <gloriousohwojeheri608@gmail.com>
Purpose: Define a Square class
"""


from turtle import pos


class Square(object):
    """ A class represents / defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """Gets the size of the square."""
        return self._Square__size

    @size.setter
    def size(self, value):
        """Initialize the square with given valuee."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """
        Calculate and return the area of the square.
        :return: The area of the square as an integer.
        """
        return self._Square__size * self._Square__size

    def my_print(self):
        """prints in stdout the square with the character #
        if size is equal to 0, prints an empty line
        """
        if self._Square__size == 0:
            print(end="\n")

        for i in range(self._Square__size):
            print("#" * self._Square__size, end="\n")
