#!/usr/bin/python3
"""This module finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers"""
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return list_of_integers[n - 1]
    low, high = 0, n - 2
    mid = (low + high) // 2
    while low <= high:
        if list_of_integers[mid] >= list_of_integers[mid - 1] and\
           list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
