#!/usr/bin/python3

def uppercase(str):
    up = ""

    for char in str:
        if char >= 'a' and char <= 'z':
            up += chr(ord(char) - 32)
        else:
            up += char
    print("{}".format(up))
