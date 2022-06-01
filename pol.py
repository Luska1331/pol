#!/usr/bin/python

# This software is in the public domain.

import sys
import math


def rainbow(i: int):
    red = int(math.sin(0.1 * float(i) + 0) * 127 + 128)
    green = int(math.sin(0.1 * float(i) + 2 * math.pi / 3) * 127 + 128)
    blue = int(math.sin(0.1 * float(i) + 4 * math.pi / 3) * 127 + 128)
    return red, green, blue


i = 0

UserInput = sys.stdin.readlines()
for line in UserInput:
    for char in line:
        r, g, b = rainbow(i)
        print(f"\033[38;2;{r};{g};{b}m{char}\033[0m", end="")
        i += 1
