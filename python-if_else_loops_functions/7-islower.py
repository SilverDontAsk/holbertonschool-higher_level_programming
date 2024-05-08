#!/usr/bin/python3
def islower(c):
    if len(c) != 1:
        raise ValueError
    return 'a' <= c <= 'z'
