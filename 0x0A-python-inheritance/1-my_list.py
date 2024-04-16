#!/usr/bin/python3
"""Define a class that inherits form class list.
"""

class MyList(list):
    """implement printing sorted"""

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        """sorted list"""
        new_list = self[:]
        new_list.sort()
        print(new_list)
