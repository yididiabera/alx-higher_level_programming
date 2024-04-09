#!/usr/bin/python3
"""A module that prints a square"""


def print_square(size):
    """A function that prints a square."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")