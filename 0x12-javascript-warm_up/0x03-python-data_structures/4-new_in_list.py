#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for item in my_list:
        new_list.append(item)
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
