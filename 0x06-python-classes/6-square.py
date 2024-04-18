#!/usr/bin/python3
"""
Author: Glorious Oyovwuvwe Ohwojeheri <gloriousohwojeheri608@gmail.com>
Purpose: Define a Square class
"""


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

        if isinstance(position, tuple):
            index = 0
            for a in position:
                index += 1

            if index > 2 or index < 2:
                raise TypeError("position must be a tuple of 2 positive integers")

            for i in range(2):
                if not isinstance(position[i], int):
                    raise TypeError("position must be a tuple of 2 positive integers")
                elif position[i] < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")

            self._Square__position = position
        else:
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

    @property
    def position(self):
        """Gets the position of spaces on square"""
        return self._Square__position
    
    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            for a in value:
                index += 1

            if index > 2 or index <= 0:
                raise TypeError("position must be a tuple of 2 positive integers")

            for i in range(2):
                if not isinstance(value[i], int):
                    raise TypeError("position must be a tuple of 2 positive integers")
                elif value[i] < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")

            self._Square__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculate and return the area of the square.
        :return: The area of the square as an integer.
        """
        return self._Square__size * self._Square__size

    def my_print(self):
        """prints in stdout the square with the character #
        position should be use by using space
        """
        if self._Square__size == 0:
            print(end="\n")

        for i in range(self._Square__size):
            if self._Square__position[1] == 0:
                print(" " * self._Square__position[0], end="")
            print("#" * self._Square__size, end="\n")
        if self._Square__position[1] > 0:
            print(" " * self._Square__position[1], end="")
