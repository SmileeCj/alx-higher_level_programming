#!/usr/bin/python3
def pow(a, b):
    n = 1

    for i in range(abs(b)):
        n *= a
    if b == 0:
        return 1
    elif b > 0:
        return n
    else:
        return 1 / n
