#!/usr/bin/python3
"""Defining a Rectangle subclass
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a Square class"""

    def __init__(self, size):
        """Initializing  the rectangle class."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculating an area of rectangle"""
        return self.__size * self.__size

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__size, self.__size)
