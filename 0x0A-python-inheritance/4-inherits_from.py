#!/usr/bin/python3
"""Define checking of inheritance"""

def inherits_from(obj, a_class):
    """module checking for subclass"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
