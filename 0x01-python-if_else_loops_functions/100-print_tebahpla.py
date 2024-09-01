#!/usr/bin/python3
for i in range(122, 96, -1):
    n = 0

    if i % 2 > 0:
        n = 32

    print(f"{i - n:c}", end="")
