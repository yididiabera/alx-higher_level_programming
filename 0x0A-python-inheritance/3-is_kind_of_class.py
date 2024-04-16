#!/usr/bin/python3
"""Define class or inhertance checker"""

def is_kind_of_class(obj, a_class):
    """checking for same or inheritance class cases"""
    if isinstance(obj, a_class):
        return True
    return False
