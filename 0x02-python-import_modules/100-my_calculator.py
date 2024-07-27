#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub as s, mul as m, div as d
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if sys.argv[2] == ("+"):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == ("-"):
        print("{} - {} = {}".format(a, b, s(a, b)))
    elif op == ("*"):
        print("{} * {} = {}".format(a, b, m(a, b)))
    elif op == ("/"):
        print("{} / {} = {}".format(a, b, d(a, b)))
