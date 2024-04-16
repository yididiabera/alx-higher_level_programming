#!/usr/bin/python3
"""Defines a class with methods
"""

class BaseGeometry:
    """represent class with methods"""

    def area(self):
        """Not imlemeted area method"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validator function"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
