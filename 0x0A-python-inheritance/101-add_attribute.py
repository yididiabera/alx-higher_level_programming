#!/usr/bin/python3
"""addition of attributes to the object."""


def add_attribute(obj, att, value):
    """This function attempts to add a new attribute to an object, provided that it's feasible.

    Parameters:

    obj (any): The object to which the attribute should be added.
    att (str): The name of the attribute to be added to obj.
    value (any): The value assigned to the attribute att.
    Raises:

        TypeError: If it's not possible to add the attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)