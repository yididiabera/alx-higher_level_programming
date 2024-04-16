#!/usr/bin/python3
"""A student class
"""


class Student:
    """A function student class
    """

    def __init__(self, first_name, last_name, age):
        """A method that is a constructor for a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """search and find a dictionary representation of a Student"""
        my_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return my_dict
