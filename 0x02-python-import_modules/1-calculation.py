#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add as ad, sub as s, mul as m, div as d

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, (ad(a, b))))
    print("{} - {} = {}".format(a, b, (s(a, b))))
    print("{} * {} = {}".format(a, b, (m(a, b))))
    print("{} / {} = {}".format(a, b, (d(a, b))))
