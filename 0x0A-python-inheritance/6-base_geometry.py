#!/usr/bin/python3
"""Define class with a problematic method
"""

class BaseGeometry:
    """Raises exception"""

    def area(self):
        """Not implemented"""
        raise Exception('area() is not implemented')
