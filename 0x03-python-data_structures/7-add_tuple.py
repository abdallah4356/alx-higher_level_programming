#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a < 2:
        if tuple_a(0) == "\0":
            tuple_a(0) = 0
        elif tuple_a(1) == "\0":
            tuple_a(1) = 0
    elif tuple_b < 2:
        if tuple_b(0) == "\0":
            tuple_b(0) = 0
        elif tuple_b(1) == "\0":
            tuple_b(1) = 0

    new = tuple_a(0) + tuple_b(0), tuple_a(1) + tuple_b(1)
    return new
