#!/usr/bin/python3
"""Define a function that check classes
"""

def is_same_class(obj, a_class):
    """checking for the same object"""
    if not type(obj) == a_class:
        return False
    else:
        return True
