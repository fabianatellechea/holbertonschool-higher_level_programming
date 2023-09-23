#!/usr/bin/python3

for i in range(122, 96, -2):
    c = i - 1
    c -= 32
    print("{}{}".format(chr(i), chr(c)), end='')
