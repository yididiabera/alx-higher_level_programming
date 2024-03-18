#!/usr/bin/python3
def multiple_returns(sentence):
    fir_char = None
    length = len(sentence)
    if length == 0:
        fir_char = None
    else:
        fir_char = sentence[0]
    return length, fir_char
