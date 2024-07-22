#!/usr/bin/python3

def add(a, b):
    r = abs(a + b)

    if a < 0 and b < 0:
        return -r

    return r
