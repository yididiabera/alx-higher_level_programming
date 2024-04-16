#!/usr/bin/python3
"""Define a Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a  Square class"""

    def __init__(self, size):
        """Intializing a class."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculating an area of rectangle"""
        return self.__size * self.__size
