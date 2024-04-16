#!/usr/bin/python3
""" a function that contains a student class"""

class Student:
    """ A student class"""

    def __init__(self, first_name, last_name, age):
        """A method that initializing a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """search and find a dictionary representation of a student class"""
        my_dict = {}
        if isinstance(attrs, list):
            if "first_name" in attrs:
                my_dict["first_name"] = self.first_name
            if "last_name" in attrs:
                my_dict["last_name"] = self.last_name
            if "age" in attrs:
                my_dict["age"] = self.age
        else:
            my_dict["first_name"] = self.first_name
            my_dict["last_name"] = self.last_name
            my_dict["age"] = self.age
        return my_dict
