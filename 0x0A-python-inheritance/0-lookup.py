#!/usr/bin/python3
"""Defines an object attribute lookup fucntion.
"""


def lookup(obj):
    """Retturn list objects"""
    keys = dir(obj)
    return keys
