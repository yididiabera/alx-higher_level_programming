#!/usr/bin/python3
def remove_char_at(str, n):
    x = 0
    new_str = ""
    while x != len(str):
        if x == n:
            pass
        else:
            new_str += str[x]
        x += 1
    return new_str