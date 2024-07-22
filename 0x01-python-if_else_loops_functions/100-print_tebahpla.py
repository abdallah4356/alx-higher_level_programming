#!/usr/bin/python3

for i in range(25, -1, -1):
    if i % 2 == 0:
        print("{}".format(chr(122 - i)), end="")

    else:
        print("{}".format(chr(90 - i)), end="")
