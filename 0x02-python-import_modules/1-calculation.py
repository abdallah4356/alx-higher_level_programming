#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div as ad, s, m, d

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, (ad(a, b))))
    print("{} - {} = {}".format(a, b, (s(a, b))))
    print("{} * {} = {}".format(a, b, (m(a, b))))
    print("{} / {} = {}".format(a, b, (d(a, b))))
