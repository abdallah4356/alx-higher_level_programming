#!/usr/bin/python3

def print_last_digit(number):
    number = int(number)

    ld = abs(number) % 10

    print(ld, end = "")
    return ld
