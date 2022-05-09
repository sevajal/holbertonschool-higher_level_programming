#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first = 0
    else:
        first = sentence[0]
    tuple = (length, first)
    return (tuple)
