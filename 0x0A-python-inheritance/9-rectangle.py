#!/usr/bin/python3
"""Defines a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Reprsent rectangle class using BaseGeometry"""

    def __init__(self, width: int, height: int):
        """Initializing the rectangle class."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self) -> int:
        """Calculating the  area of rectangle"""
        return self.__width * self.__height

    def __str__(self) -> str:
        """It returns the string representation of Rectangle"""
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
