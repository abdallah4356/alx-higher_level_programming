#!/usr/bin/python3

def uppercase(str):
   up = ""

for char in str:
    if char >= 'a' and char <= 'z':
        up += ord(char) - 32
    else:
        up += (char)
    print(up)
