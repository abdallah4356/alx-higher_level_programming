#!/usr/bin/python3

def pow(a, b):
    if b > 0:
        r = 1
        for i in range(b):
            r *= a
        return r
    elif b < 0:
        r = 1
        for i in range(-b):
            r *= a
        return 1 / r
