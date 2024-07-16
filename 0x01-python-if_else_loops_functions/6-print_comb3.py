#!/usr/bin/python3

for i in range(0, 9):
    for y in range(1, 10):
        if i != y:
            if i != 8 or y != 9:
                print(f"{i}{y}", end=', ')
            else:
                print(f"{i}{y}")
