#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    _sum = 0

    for x in range(1, n + 1):
        _sum = _sum + int(sys.argv[x])

    print("{}".format(_sum))
